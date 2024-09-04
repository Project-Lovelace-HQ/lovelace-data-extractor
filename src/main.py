import logging
import azure.functions as func
import json

import requests
from src.data_extractor.extract_game_data import extract_game_data
from src.ludopedia_website.fetch_boardgame_by_url import fetch_boardgame_by_url

bp = func.Blueprint()


class ResponseSubscribedGamesUpdatedData:
    def __init__(self, id, error, response):
        self.id = id
        self.error = error
        self.response = response

    def to_dict(self):
        return {"id": self.id, "error": self.error, "response": self.response}


@bp.function_name(name="LovelaceDataExtractor")
@bp.route(route="LovelaceDataExtractor")
def LovelaceDataExtractor(req: func.HttpRequest) -> func.HttpResponse:
    try:
        req_body = req.get_json()
    except ValueError:
        error_message = "Invalid JSON received"
        logging.error(error_message)
        return func.HttpResponse(
            error_message,
            status_code=400,
        )

    if not req_body:
        error_message = "Empty request array received"
        logging.error(error_message)
        return func.HttpResponse(
            error_message,
            status_code=400,
        )

    responses = []
    for item in req_body:
        if not isinstance(item, dict) or "url" not in item or "id" not in item:
            error_message = "Each item in the JSON array must contain 'url' and 'id'"
            logging.error(error_message)
            return func.HttpResponse(
                error_message,
                status_code=422,
            )

        url = item.get("url") + "?v=anuncios"
        id = item.get("id")
        if url and id:
            try:
                game_data_list = fetch_boardgame_by_url(url)

                if isinstance(game_data_list, str):
                    response_data = game_data_list

                if isinstance(game_data_list, list):
                    response_data = extract_game_data(game_data_list)

                responses.append(
                    ResponseSubscribedGamesUpdatedData(
                        id, False, response_data
                    ).to_dict()
                )
            except requests.exceptions.HTTPError as errh:
                error_message = "HTTP Error:" + str(errh)
                logging.error(error_message)
            except requests.exceptions.ConnectionError as errc:
                error_message = "Error Connecting:" + str(errc)
                logging.error(error_message)
            except requests.exceptions.Timeout as errt:
                error_message = "Timeout Error:" + str(errt)
                logging.error(error_message)
            except requests.exceptions.RequestException as err:
                error_message = "Something went wrong" + str(err)
                logging.error(error_message)
            except Exception as e:
                error_message = f"Error fetching data from {url}"
                logging.error(error_message)
                responses.append(
                    ResponseSubscribedGamesUpdatedData(id, True, e).to_dict()
                )

    logging.info(f"Responses: {responses}")

    json_string_response = json.dumps(responses)

    return func.HttpResponse(
        json_string_response,
        status_code=200,
    )
