# Pytest Allure Report Example

This repo contains the sample code for the article - [How To Create Interactive Test Reports with Pytest and Allure](https://pytest-with-eric.com/reporting/pytest-allure-report/)


## Requirements
* Python (3.12)
* Allure Report

## Installation

To install the project, you need to have Poetry installed. If you don't have it installed, you can install it by following the instructions [here](https://python-poetry.org/docs/#installation).

## Usage

To generate the allure reports, you can use the following command:

```bash
$ poetry run pytest --alluredir=allure-results
```

To view the allure reports, you can use the following command:

```bash
$ poetry run allure serve allure-results
```

If you have any questions about the project please raise an Issue on GitHub.