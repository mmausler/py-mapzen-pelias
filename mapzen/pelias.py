#!/usr/bin/env python

import sys
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

        print params
        rsp = requests.get(url, params=params)

        if more.get('raw', False):
            return rsp.content

        data = geojson.loads(rsp.content)
        return data

class formatter:

    def __init__(self, data):

        self.data = data

    def markdown(self, fh=sys.stdout):

        fh.write("## Bounding box\n\n")
        fh.write("%s\n\n" % self.data['bbox'])

        fh.write("## Features\n\n")

        for f in self.data['features']:
        
            props = f.get('properties', {})
    
            fh.write("### %s\n\n" % f['type'])

            fh.write("#### Geometry\n\n")
            fh.write("%s\n\n" % f['geometry'])        
            
            fh.write("#### Properties\n\n")
            
            for k,v in props.items():
                fh.write("* `%s` %s\n" %(k, v))
                
            fh.write("\n")


if __name__ == '__main__':

    method = 'search'
    params = {'input':'montreal'}
    
    a = api()
    rsp = a.execute_method(method, params)

    f = formatter(rsp)
    f.markdown()
