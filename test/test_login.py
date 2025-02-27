import pytest
from src.espocrm_api.endpoint import Endpoint
from src.assertions.status_code_assertions import AssertionStatusCode
from src.resources.authentifications.authentification import Auth
from src.espocrm_api.api_request import EspocrmRequest


@pytest.mark.smoke
def test_valid_login(get_headers):
    headers = Auth().get_valid_user_headers(get_headers)
    response = EspocrmRequest().get(Endpoint.login(), headers)
    AssertionStatusCode().assert_status_code_200(response)


@pytest.mark.smoke
def test_invalid_login(get_headers):
    headers = Auth().get_invalid_user_headers(get_headers)
    response = EspocrmRequest().get(Endpoint.login(), headers)
    AssertionStatusCode().assert_status_code_401(response)
