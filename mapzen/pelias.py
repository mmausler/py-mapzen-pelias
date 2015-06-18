#!/usr/bin/env python

import requests
import geojson
import logging

# http://pelias.mapzen.com/

class api:

    def __init__ (self, **kwargs):

        self.host = kwargs.get('host', 'pelias.mapzen.com/')
        self.proxy = kwargs.get('proxy', None)

    def execute_method(self, method, params, **more):

        method = method.lstrip('/')
        url = "https://" + self.host + method

        rsp = requests.get(url, params=params)

        if more.get('raw', False):
            return rsp.content

        data = geojson.loads(rsp.content)
        return data

if __name__ == '__main__':

    method = 'search'
    params = {input:'montreal'}

    a = api()
    rsp = a.execute_method(method, params)

    print rsp
