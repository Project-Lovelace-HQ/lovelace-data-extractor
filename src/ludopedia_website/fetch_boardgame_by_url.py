from bs4 import BeautifulSoup
import requests

from src.util.subscribed_game_updated_data import SubscribedGameUpdatedData


def fetch_boardgame_by_url(url):
    # Make a GET request to the URL
    # URL Example - "https://ludopedia.com.br/jogo/frostpunk-the-board-game?v=anuncios"
    response = requests.get(url)
    response.raise_for_status()

    if response is None:
        # throw exception
        raise Exception("Error: Couldn't fetch the URL - " + url)

    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the table with the 'table' class
    table = soup.find("table", {"class": "table"})

    # Check if the table was found
    if table is None:
        # throw exception
        raise Exception("Error: Couldn't find the table in the URL - " + url)

    # Get the headers of the table
    headers = [header.text for header in table.find_all("th")]

    # Get the index of the relevant columns
    product_type_index = headers.index("Produto")
    city_index = headers.index("Cidade")
    condition_index = headers.index("Condição")
    details_index = headers.index("Obs")
    price_index = headers.index("Valor")
    link_index = headers.index("Link")

    # Find all rows in the table
    rows = table.find_all("tr")

    # Check if the table has any rows
    if not rows:
        # Return an warning if there are no games for sale
        return "Indisponível"

    # Create an empty list to store the rows
    data = []

    # Iterate over the rows in the tbody of the table
    for row in rows:
        columns = row.find_all("td")

        # Check if the row has columns
        if columns:
            # Get the values from each column
            product_type = columns[product_type_index].text.strip()
            city = columns[city_index].text.strip()
            condition = columns[condition_index].text.strip()
            details = columns[details_index].text.strip()
            price = columns[price_index].text.strip()
            link = columns[link_index].text.strip()

            # Filter only the data with product_type "Jogo"
            if product_type == "Jogo" and link == "Anúncio":
                game_data_object = SubscribedGameUpdatedData(
                    product_type, city, condition, details, price, link
                )
                data.append(game_data_object.to_dict())

    # Return the data list
    return data
