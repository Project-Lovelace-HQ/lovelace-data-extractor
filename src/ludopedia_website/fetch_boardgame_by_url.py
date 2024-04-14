from bs4 import BeautifulSoup
import requests


class SubscribedGameUpdatedData:
    def __init__(self, city, condition, details, price, link):
        self.city = city
        self.condition = condition
        self.details = details
        self.price = price
        self.link = link

    def to_dict(self):
        return {
            "city": self.city,
            "condition": self.condition,
            "details": self.details,
            "price": self.price,
            "link": self.link,
        }


def fetch_boardgame_by_url(url):
    # Make a GET request to the URL
    # URL Example - "https://ludopedia.com.br/jogo/frostpunk-the-board-game?v=anuncios"
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the table with the 'table' class
    table = soup.find("table", {"class": "table"})

    # Get the headers of the table
    headers = [header.text for header in table.find_all("th")]

    # Get the index of the relevant columns
    city_index = headers.index("Cidade")
    condition_index = headers.index("Condição")
    details_index = headers.index("Obs")
    price_index = headers.index("Valor")
    link_index = headers.index("Link")

    # Create an empty list to store the rows
    data = []

    # Iterate over the rows in the tbody of the table
    for row in table.find_all("tr"):
        columns = row.find_all("td")

        # Check if the row has columns
        if columns:
            # Get the values from each column
            city = columns[city_index].text.strip()
            condition = columns[condition_index].text.strip()
            details = columns[details_index].text.strip()
            price = columns[price_index].text.strip()
            link = columns[link_index].text.strip()

            game_data_object = SubscribedGameUpdatedData(
                city, condition, details, price, link
            )
            data.append(game_data_object.to_dict())

    # Return the data list
    return data
