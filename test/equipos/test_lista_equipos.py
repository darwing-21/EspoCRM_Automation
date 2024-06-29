import pytest
from config import BASE_URI
from src.assertions.equipos_assertions import AssertionEquipos
from src.assertions.schema_assertions import AssertionSchemas
from src.espocrm_api.api_request import EspocrmRequest
from src.espocrm_api.endpoint import Endpoint


def test_lista_equipos_con_datos_exitoso(get_headers):
    url = f'{BASE_URI}{Endpoint.LISTA_EQUIPOS.value}'
    headers = get_headers("admin", "admin")
    response = EspocrmRequest().get(url, headers=headers)
    AssertionEquipos().assert_status_code(response, 200)
    AssertionSchemas().assert_equipo_lista_schema_file(response.json())


def test_lista_equipos_sin_datos_exitoso(get_headers):
    url = f'{BASE_URI}{Endpoint.LISTA_EQUIPOS.value}'
    headers = get_headers("sinequipos", "hola")
    response = EspocrmRequest().get(url, headers=headers)
    AssertionEquipos().assert_status_code(response, 200)
    AssertionSchemas().assert_equipo_lista_schema_file(response.json())
    AssertionEquipos().assert_empty_list(response.json(), "list")
    AssertionEquipos().assert_total_equals(response.json(), 0)


def test_lista_equipos_sin_select(get_headers):
    url = f'{BASE_URI}{Endpoint.LISTA_EQUIPOS_SIN_SELECT.value}'
    headers = get_headers("chars_dar", "password")
    response = EspocrmRequest().get(url, headers=headers)
    AssertionEquipos().assert_status_code(response, 200)
    AssertionSchemas().assert_equipo_sin_select_schema_file(response.json())


def test_lista_equipos_autenficacion_invalida(get_headers):
    url = f'{BASE_URI}{Endpoint.LISTA_EQUIPOS.value}'
    headers = get_headers("chars_dar", "incorrecto")
    response = EspocrmRequest().get(url, headers=headers)
    AssertionEquipos().assert_status_code(response, 401)


def test_lista_equipos_select_desconocido(get_headers):
    url = f'{BASE_URI}{Endpoint.LISTA_EQUIPOS_SELECT_DESCONOCIDO.value}'
    headers = get_headers("chars_dar", "password")
    response = EspocrmRequest().get(url, headers=headers)
    AssertionEquipos().assert_status_code(response, 200)
    AssertionSchemas().assert_equipo_lista_schema_file(response.json())


def test_lista_equipos_sin_autorizacion(get_headers):
    url = f'{BASE_URI}{Endpoint.LISTA_EQUIPOS.value}'
    headers = get_headers("sin_autorizacion", "password")
    response = EspocrmRequest().get(url, headers=headers)
    AssertionEquipos().assert_status_code(response, 403)


def test_lista_equipos_sin_autorizacion(get_headers):
    url = f'{BASE_URI}{Endpoint.LISTA_EQUIPOS.value}'
    headers = get_headers("sin_autorizacion", "password")
    response = EspocrmRequest().get(url, headers=headers)
    AssertionEquipos().assert_status_code(response, 403)


def test_lista_equipos_maxsize_mayor_al_total(get_headers):
    url = f'{BASE_URI}{Endpoint.LISTA_EQUIPOS_MAXSIZE_MAYOR_TOTAL.value}'
    headers = get_headers("chars_dar", "password")
    response = EspocrmRequest().get(url, headers=headers)
    AssertionEquipos().assert_status_code(response, 200)
    AssertionSchemas().assert_equipo_lista_schema_file(response.json())


def test_lista_equipos_offser_mayor_al_total(get_headers):
    url = f'{BASE_URI}{Endpoint.LISTA_EQUIPOS_OFFSET_MAYOR_TOTAL.value}'
    headers = get_headers("chars_dar", "password")
    response = EspocrmRequest().get(url, headers=headers)
    AssertionEquipos().assert_status_code(response, 200)
    AssertionSchemas().assert_equipo_lista_schema_file(response.json())
    AssertionEquipos().assert_empty_list(response.json(), "list")


def test_lista_equipos_orden_asc(get_headers):
    url = f'{BASE_URI}{Endpoint.LISTA_EQUIPOS_ORDEN_ASC.value}'
    headers = get_headers("chars_dar", "password")
    response = EspocrmRequest().get(url, headers=headers)
    AssertionEquipos().assert_status_code(response, 200)
    AssertionSchemas().assert_equipo_lista_schema_file(response.json())
    AssertionEquipos().assert_check_orden(response.json(), 'asc')

def test_lista_equipos_orden_desc(get_headers):
    url = f'{BASE_URI}{Endpoint.LISTA_EQUIPOS_ORDEN_DESC.value}'
    headers = get_headers("chars_dar", "password")
    response = EspocrmRequest().get(url, headers=headers)
    AssertionEquipos().assert_status_code(response, 200)
    AssertionSchemas().assert_equipo_lista_schema_file(response.json())
    AssertionEquipos().assert_check_orden(response.json(), 'desc')
