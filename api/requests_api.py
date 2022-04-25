from wsgiref import headers
from xmlrpc.client import ResponseError
import requests

class RequestsApi:
    url = 'http://127.0.0.1:5000'

    @staticmethod
    def get_api(title):
        try:
            response = requests.request("GET", RequestsApi.url + '/peli?title=' + str(title))
            if response.status_code != 200:
                return False
            else:
                return response.content
        except:    
            return False       