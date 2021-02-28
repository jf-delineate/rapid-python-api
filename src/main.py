from fastapi import FastAPI
from fastapi import Response
from loguru import logger
import constants
import os
import requests
import sys
import toml


def get_config_file(file_name):
    dir = os.path.dirname(os.path.realpath(__file__))
    return dir + "/" + file_name


def start_app():
    logger.remove()
    logger.add(sys.stderr, level="DEBUG")
    return FastAPI()


config = toml.load(get_config_file("config.toml"))
secrets = toml.load(get_config_file(".secrets.toml"))
app = start_app()


@app.get("/healthz")
def healthz():
    pass


@app.get("/company/{company_id}")
def get_company(company_id, response: Response):
    status_code, json = query_company_address(company_id)
    response.status_code = status_code
    return json


def query_company_address(company_id):

    response_json = None
    status_code, json = query_company(company_id)

    if status_code == 200:
        if constants.REGISTERED_OFFICE_ADDRESS not in json:
            status_code = constants.HTTP_NOT_FOUND
        else:
            response_json = json[constants.REGISTERED_OFFICE_ADDRESS]

    return status_code, response_json


def query_company(company_id):

    # companies_house, endole
    url = config["api"]["companies_house"]["api_url"].format(company_id)
    headers = {"Authorization": secrets["api"]["companies_house"]["api_key"]}
    response = requests.get(url, headers=headers)
    return response.status_code, response.json()
