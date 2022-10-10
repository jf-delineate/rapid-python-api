"""This module implements an example API using FastAPI"""
import os
import sys
import requests
import toml
import bleach
from fastapi import FastAPI
from fastapi import Response
from loguru import logger
import constants


def get_config_file(file_name):
    """This function gets the config file path

    Args:
        file_name (string): relative path and file name

    Returns:
        string: full path to the config file
    """
    folder = os.path.dirname(os.path.realpath(__file__))
    return folder + "/" + file_name


def start_app():
    """_summary_

    Returns:
        _type_: _description_
    """
    logger.remove()
    logger.add(sys.stderr, level="DEBUG")
    return FastAPI()


config = toml.load(get_config_file("config.toml"))
secrets = toml.load(get_config_file(".secrets.toml"))
app = start_app()


@app.get("/healthz")
def healthz():
    """Liveliness probe using the Google standard"""


@app.get("/company/{company_id}")
def get_company(company_id, response: Response):
    """Gets company address using the unique id

    Args:
        company_id (string): The unique ID for the company
        response (Response): The response for the request

    Returns:
        json: The company address as json
    """
    status_code, json = query_company_address(company_id)
    response.status_code = status_code
    return bleach.clean(json)


def query_company_address(company_id):
    """Queries the company details

    Args:
        company_id (string): The unique ID for the company

    Returns:
        int: The HTTP status code
        json: The company address as json
    """
    response_json = None
    status_code, json = query_company(company_id)

    if status_code == 200:
        if constants.REGISTERED_OFFICE_ADDRESS not in json:
            status_code = constants.HTTP_NOT_FOUND
        else:
            response_json = json[constants.REGISTERED_OFFICE_ADDRESS]

    return status_code, response_json


def query_company(company_id):
    """Queries the company details from the extrenal endpoint

    Args:
        company_id (string): The unique ID for the company

    Returns:
        int: The HTTP status code
        json: The company details as json
    """
    url = config["api"]["companies_house"]["api_url"].format(company_id)
    headers = {"Authorization": secrets["api"]["companies_house"]["api_key"]}
    response = requests.get(url, headers=headers, timeout=500)
    return response.status_code, bleach.clean(response.json())
