# -*- coding: utf-8 -*-
# filename: main.py
import web

urls = (
    '/hello', 'SayHello',
)

app = web.application(urls, globals())

class SayHello(object):
    def GET(self):
        return 'Hello!'

if __name__ == '__main__':
    app.run()