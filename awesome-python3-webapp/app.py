# Created by PyCharm.
# User: zhangrxiang
# Date: 2017/1/9
# Time: 23:21
# File: 
# Project: python3
# Location: Wuxi

import logging
logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from aiohttp import web


def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html', charset='UTF-8')


@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 8808)
    logging.info('server started at http://127.0.0.1:8808...')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
