# -*- coding: utf-8 -*-

from py4web.core import Fixture, HTTP
from py4web import request, response
from inspect import signature, _empty
import json

def unjson(value):
    try:
        return json.loads(value)
    except (json.decoder.JSONDecodeError, TypeError,):
        return value

def webio(func, **defaults):
    kwargs = {}
    sign = signature(func).parameters
    for key,parameter in sign.items():
        if parameter.default==_empty:
            if key in request.query:
                kwargs[key] = unjson(request.query[key])
            elif request.json and (key in request.json):
                kwargs[key] = request.json[key]
            elif key in defaults:
                kwargs[key] = defaults[key]

        elif key in request.query:
            kwargs[key] = unjson(request.query[key])
        elif request.json and (key in request.json):
            kwargs[key] = request.json[key]
        elif key in defaults:
            kwargs[key] = defaults[key]
        else:
            kwargs[key] =  parameter.default

    if not request.query is None:
        kwargs.update({k: unjson(v) for k,v in request.query.items() if not k in sign})
    elif not request.json is None:
        kwargs.update({k: v for k,v in request.json.items() if not k in sign})
    kwargs.update({k: v for k,v in defaults.items() if not k in sign})
    return kwargs

class WebWrapper(Fixture):
    """docstring for WebWrapper."""

    def __init__(self, **defaults):
        super(WebWrapper, self).__init__()
        self.defaults = defaults
        self.update = self.defaults.update
        self.__setitem__ = self.defaults.__setitem__

    def parse_request(self, func):
        return webio(func, **self.defaults)

    def __call__(self, func):
        def wrapper():
            return func(**webio(func, **self.defaults))
        return wrapper


def brap(**defaults):
    """ web wrapper
    Variables declared in function signature will be taken from request and
    decoded as they were json string before being passed to the function.

    defaults : Default values that will overwrite the ones defined in signature.
    """
    def decorator(func):
        def wrapper():
            kwargs = {}
            sign = signature(func).parameters
            for key,parameter in sign.items():
                if parameter.default==_empty:
                    if key in request.query:
                        kwargs[key] = unjson(request.query[key])
                    elif request.json and (key in request.json):
                        kwargs[key] = request.json[key]
                    elif key in defaults:
                        kwargs[key] = defaults[key]

                elif key in request.query:
                    kwargs[key] = unjson(request.query[key])
                elif request.json and (key in request.json):
                    kwargs[key] = request.json[key]
                elif key in defaults:
                    kwargs[key] = defaults[key]
                else:
                    kwargs[key] =  parameter.default

            if not request.query is None:
                kwargs.update({k: unjson(v) for k,v in request.query.items() if not k in sign})
            elif not request.json is None:
                kwargs.update({k: v for k,v in request.json.items() if not k in sign})
            kwargs.update({k: v for k,v in defaults.items() if not k in sign})

            return func(**kwargs)
        return wrapper
    return decorator

class LocalsOnly(Fixture):
    """docstring for LocalsOnly."""

    def __init__(self):
        super(LocalsOnly, self).__init__()
        # self.request = request

    def on_request(self):
        if not request.urlparts.netloc.startswith('localhost'):
            raise HTTP(403)


class CORS(Fixture):
    """ Fixture helper for sharing web service avoiding cross origin resource sharing problems """

    def __init__(self, age=86400, origin="*", headers="*", methods="*"):
        super(CORS, self).__init__()
        self.age = age
        self.origin = origin
        self.headers = headers
        self.methods = methods

    def on_request(self):
        response.headers["Access-Control-Allow-Origin"] = self.origin
        response.headers["Access-Control-Max-Age"] = self.age
        response.headers["Access-Control-Allow-Headers"] = self.headers
        response.headers["Access-Control-Allow-Methods"] = self.methods
        response.headers["Access-Control-Allow-Credentials"] = "true"
