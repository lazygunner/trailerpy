from flask import Flask, request
from flask.ext import restful
from xunleipy.remote import XunLeiRemote


app = Flask(__name__)
api = restful.Api(app)

u = ''
p = ''


class RemoteDownloadTrailers(restful.Resource):
    def get(self):
        return {'data': 'welcome'}

    def post(self):
        xlr = XunLeiRemote(u, p)
        peer_list = xlr.get_remote_peer_list()
        pid = peer_list[0]['pid']
        download_link = request.form['download_link']
        ret = xlr.add_urls_to_remote(pid, 'C:/MovieTrailers/', [download_link])
        return ret

api.add_resource(RemoteDownloadTrailers, '/')

if __name__ == '__main__':
    app.run(debug=True)
