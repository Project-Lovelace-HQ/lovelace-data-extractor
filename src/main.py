import logging
import azure.functions as func
import json
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

                if game_data_list is None:
                    responses.append(
                        ResponseSubscribedGamesUpdatedData(
                            id, True, "Erro na busca"
                        ).to_dict()
                    )
                    return

                if isinstance(game_data_list, str):
                    response_data = game_data_list

                if isinstance(game_data_list, list):
                    response_data = extract_game_data(game_data_list)

                responses.append(
                    ResponseSubscribedGamesUpdatedData(
                        id, False, response_data
                    ).to_dict()
                )
            except Exception as e:
                error_message = f"Error fetching data from {url}"
                logging.error(f"{error_message}: {e}")
                responses.append(
                    ResponseSubscribedGamesUpdatedData(
                        id, True, f"{error_message}: {e}"
                    ).to_dict()
                )

    logging.info(f"Responses: {responses}")

    json_string_response = json.dumps(responses)

    return func.HttpResponse(
        json_string_response,
        status_code=200,
    )
