# -*- encoding:utf-8 -*-

import json

from flask import Flask, request
from flask.ext import restful
from xunleipy.remote import XunLeiRemote


app = Flask(__name__)
api = restful.Api(app)

u = ''
p = ''


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


class HelloWorld(restful.Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        xlr = XunLeiRemote(u, p)
        peer_list = xlr.get_remote_peer_list()
        pid = peer_list[0]['pid']
        download_link = json.loads(request.data).get('download_link', '')
        ret = xlr.add_urls_to_remote(pid, 'C:/MovieTrailers/', [download_link])
        print ret
        return ret

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
