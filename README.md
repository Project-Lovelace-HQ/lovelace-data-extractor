# LOVELACE DATA EXTRACTOR

This project is part of **Project Lovelace**, aiming to develop a price tracker for the [Ludopedia](https://ludopedia.com.br/) website, where a user can specify which games they want to track via a [Notion](https://www.notion.so) database.

**Lovelace Data Extractor** is an Azure Function app for interacting with the Ludopedia website to get the user's subscribed games info from the URL submitted in the Notion database through the [Lovelace Data Sync](https://github.com/Project-Lovelace-HQ/lovelace-data-sync) service. It is built with Python.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Installing and Running this Project

For this project, you will need **Python** in version 3.8+ and **Pipenv**. [How to install Pipenv?](https://pipenv.pypa.io/en/latest/installation.html)

1. Clone the repository
2. Install the dependencies with `pipenv install`
3. Setup the Git Hooks with `pre-commit install`
4. Generate the virtual environment with `python -m venv .venv`
5. Copy the `local.settings.example.json` file to `local.settings.json` (no changes needed)
6. Install the [Azurite](https://marketplace.visualstudio.com/items?itemName=Azurite.azurite) extension for VSCode and run the `Azurite: Start` command
7. Install the [Azure Functions](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions) extension for VSCode and run the project in debug mode, then you are ready to run the function using the URL in the console!

> [!IMPORTANT]
> - You will be prompted to install the Azure Functions Core Tools if using VSCode. If not, install it manually.
> - You will need a way to do Http Requests to test the application.

### Endpoints available

#### POST `/LovelaceDataExtractor`

Fetch the Ludopedia games available for sale.

**Request Body**

- URL: `"url": "<game-url-on-ludopedia>"` for fetching the price and data.
- ID: `"id": "<figma id for the game page>"` for updating it with the current data.

**Examples**

Request

```json
POST <AZURE_URL>/api/LovelaceDataExtractor

[
    {
        "url": "https://ludopedia.com.br/jogo/nemesis",
        "id": "696e89cd-5980-48fa-aba8-610e21d77b21"
    }
]
```

Response

```json
STATUS CODE: 200

[
	{
		"id": 1,
		"error": false,
		"response": {
            "city": "Rio de Janeiro",
            "condition": "Lacrado",
            "details": "",
            "price": 1.142.80,
            "link": "Anúncio"
        },
    }
]
```

### Running the application

You can run the application as local Azure Function with the following command:

```sh
invoke run
```

> Be sure to have the Azurite service up and running in your environment.

### Running the tests

You can run the tests with the following command:

```sh
invoke test
```

### Updating requirements.txt

If you change any dependencies, you will need to update the requirements.txt for the Azure Function service:

```sh
invoke requirements
```

### Extra tasks

> Check other tasks available for this project, like generating coverage, linting and versioning in the `tasks.py` file
