#!/usr/bin/env python
# -*- coding:utf-8 -*-
from wsgiref.simple_server import make_server

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return '<h1>Hello, world!</h1>'

server = make_server('0.0.0.0', 9090, application)

server.serve_forever()

