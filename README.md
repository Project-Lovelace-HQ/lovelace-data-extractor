# LOVELACE DATA EXTRACTOR

This project is part of **Project Lovelace**, aiming to develop a price tracker for the [Ludopedia](https://ludopedia.com.br/) website, where a user can specify which games they want to track via a [Notion](https://www.notion.so) database.

**Lovelace Data Extractor** is an app for interacting with the Ludopedia website to get the user's subscribed games info from the URL submitted in the Notion database through the [Lovelace Data Sync](https://github.com/Project-Lovelace-HQ/lovelace-data-sync) service. It is built with Python.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Installing and Running this Project

For this project, you will need **Python** in version 3.8+ and **Pipenv**. [How to install Pipenv?](https://pipenv.pypa.io/en/latest/installation.html)

1. Clone the repository
2. Install the dependencies with `pipenv install`
3. Setup the Git Hooks with `pre-commit install`

### Running the application

You can run the application with the following command:

```sh
invoke run
```

### Running the tests

You can run the tests with the following command:

```sh
invoke test
```

### Extra tasks

> Check other tasks available for this project, like generating coverage, linting and versioning in the `tasks.py` file
