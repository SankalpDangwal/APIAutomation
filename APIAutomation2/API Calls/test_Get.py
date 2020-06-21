import requests
import json
import jsonpath
import pytest


# class api_automation:
def test_02_getdetails():
    url = "https://reqres.in/api/users?page=2"
    response = requests.get(url)
    print(response.content)
    print(response.headers)
    print(response.status_code)
    print(response.headers.get("Data"))
    print(response.headers.get("Server"))
    assert response.status_code == 200
    print(response.cookies)
    print(response.encoding)
    print(response.elapsed)
    json_response = json.loads(response.text)
    print(json_response)
    for i in range(0, 3):
        first_name = jsonpath.jsonpath(json_response, 'data[' + str(+i) + '].first_name')
        print(first_name[0])


def test_01_post_Call():
    url = "https://reqres.in/api/login"
    header = {'email': 'eve.holt@reqres.in',
              'password': 'cityslicka'}
    response_json = requests.post(url, header)
    print(response_json)
    print(response_json.content)
    print(response_json.headers.get('Content-Length'))
    response_list = json.loads(response_json.text)
    print(response_list)
