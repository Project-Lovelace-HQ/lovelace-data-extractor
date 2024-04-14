import azure.functions as func
from src.ludopedia_website.fetch_boardgame_by_url import fetch_boardgame_by_url

bp = func.Blueprint()


@bp.function_name(name="LovelaceDataExtractor")
@bp.route(route="LovelaceDataExtractor")
def LovelaceDataExtractor(req: func.HttpRequest) -> func.HttpResponse:
    url = req.params.get("url")
    if not url:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            url = req_body.get("url")

    if url:
        response = fetch_boardgame_by_url(url)
        return response
    else:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a URL in the query string or in the request body for a personalized response.",
            status_code=200,
        )
