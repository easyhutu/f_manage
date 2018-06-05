"""
CREATE: 2018/5/14
AUTHOR:　HEHAHUTU
"""
from flask import jsonify, abort, request, Response
import json
import flask_restful
from werkzeug import exceptions
from .code import Code


def make_result(data=None, code=Code.SUCCESS):
    return jsonify({"code": code, "data": data, "message":  Code.msg[code]})
    # resp = Response()
    # resp.status_code = 200
    # resp.data = json.dumps({"code": code, "data": data, "message": Code.msg[code]})
    # return resp


def custom_abord(http_status_code, **kwargs):
    # 只要http_status_code 为400， 报参数错误
    if http_status_code == 400:
        abort(make_result(code=Code.NO_PARAM))
    # 正常返回消息
    return abort(http_status_code)
