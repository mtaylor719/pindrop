#!/usr/bin/python

import requests

try:
    import json
except ImportError:
    import simplejson as json

class client:

    def __init__(self, endpoint, port):
        self.endpoint = 'http://{}:{}'.format(endpoint, port)

    """
    Used to get all results
    """
    def all_result(self):
        return self._request('GET', '/results')

    """
    Used to get area codes
    """
    def area_code(self, area_code):
        return self._request('GET', '/results/{}/'.format(area_code))

    #Should add some authentication here
    def _request(self, method, uri, data = {}):
        full_url = '{}{}'.format(self.endpoint, uri)
        if method == 'POST':
            response = requests.request(method, full_url, verify=False, data=data)
        else:
            response = requests.request(method, full_url, verify=False, params=data)

        response.raise_for_status()
        
        content = json.loads(response.content)

        return content
            
        
