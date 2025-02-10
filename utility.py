import logging
import requests
import json
from log_utility import LoggerLayer
class UtilityClass():
    def __init__(self):

        pass

    def send_post_request(uri, body):
        response = requests.post(uri, json=body)
        if(response.status_code == 200):
            return response.json()
        else:
            return None
    
    def send_get_request(uri, params: dict):
        logger = LoggerLayer()
        logger.log_info(f'sending get request to {uri} with params {params}')
        response = requests.get(uri, params=params)
        if(response.status_code == 200):
            logging.info(f"response code is 200")
            jsonval = json.loads(response.content) 
            return jsonval['results']

        else:
            return None