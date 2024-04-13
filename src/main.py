from bs4 import BeautifulSoup
import requests
import csv
import os


# Make a GET request to the URL
url = "https://ludopedia.com.br/jogo/frostpunk-the-board-game?v=anuncios"
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find the table with the 'Produto' and 'Valor' columns
table = soup.find("table", {"class": "table"})

# Get the headers of the table
headers = [header.text for header in table.find_all("th")]

# Get the index of the columns
cidade_index = headers.index("Cidade")
condicao_index = headers.index("Condição")
obs_index = headers.index("Obs")
valor_index = headers.index("Valor")
link_index = headers.index("Link")

# Iterate over the rows in the tbody of the table
for row in table.find_all("tr"):
    columns = row.find_all("td")

    # Check if the row has columns
    if columns:
        # Get the values
        cidade = columns[cidade_index].text
        condicao = columns[condicao_index].text
        obs = columns[obs_index].text
        valor = columns[valor_index].text
        link = columns[link_index].text

        # Print these values using strip()
        print(f"Cidade: {cidade.strip()}")
        print(f"Condição: {condicao.strip()}")
        if obs:
            print(f"Obs: {obs.strip()}")
        print(f"Valor: {valor.strip()}")
        print(f"Link: {link.strip()}")
        print()

# Define the directory path
dir_path = os.path.dirname("./../output/")

# Create the directory if it does not exist
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

# Open a new CSV file in write mode
with open("./../output/results.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Write the headers to the CSV file
    writer.writerow(["Cidade", "Condição", "Obs", "Valor", "Link"])

    # Iterate over the rows in the tbody of the table
    for row in table.find_all("tr"):
        columns = row.find_all("td")

        # Check if the row has columns
        if columns:
            # Get the values
            cidade = columns[cidade_index].text.strip()
            condicao = columns[condicao_index].text.strip()
            obs = columns[obs_index].text.strip() if columns[obs_index].text else ""
            valor = columns[valor_index].text.strip()
            link = columns[link_index].text.strip()

            # Write these values to the CSV file
            writer.writerow([cidade, condicao, obs, valor, link])
