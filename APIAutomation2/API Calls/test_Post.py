import requests
import json
import jsonpath
import pytest



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

