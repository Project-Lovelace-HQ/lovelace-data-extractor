import logging
import azure.functions as func
import json
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
        return func.HttpResponse(
            "Invalid JSON received",
            status_code=400,
        )

    if not req_body:
        return func.HttpResponse(
            "Empty request array received",
            status_code=400,
        )

    responses = []
    for item in req_body:
        if not isinstance(item, dict) or "url" not in item or "id" not in item:
            return func.HttpResponse(
                "Each item in the JSON array must contain 'url' and 'id'",
                status_code=422,
            )

        url = item.get("url")
        id = item.get("id")
        if url and id:
            try:
                game_data_list = fetch_boardgame_by_url(url)
                responses.append(
                    ResponseSubscribedGamesUpdatedData(
                        id, False, game_data_list
                    ).to_dict()
                )
            except Exception:
                responses.append(
                    ResponseSubscribedGamesUpdatedData(
                        id, True, f"Error fetching data from {url}"
                    ).to_dict()
                )

    logging.info(f"Responses: {responses}")

    json_string_response = json.dumps(responses)

    return func.HttpResponse(
        json_string_response,
        status_code=200,
    )
