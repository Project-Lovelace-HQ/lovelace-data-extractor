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

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory
parent_dir = os.path.dirname(script_dir)

# Define the output directory path
output_dir = os.path.join(parent_dir, "output")

# Create the output directory if it does not exist
os.makedirs(output_dir, exist_ok=True)

# Define the path of the CSV file
csv_file_path = os.path.join(output_dir, "results.csv")

# Open the CSV file in write mode
with open(csv_file_path, "w", newline="") as file:
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
