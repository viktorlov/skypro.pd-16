from datetime import datetime

from flask import Blueprint, jsonify, request

errorhandlers = Blueprint('errorhandlers', __name__)


@errorhandlers.app_errorhandler(404)
def error_404(error):
    return jsonify({"url": request.url,
                    "status": f'{error}',
                    "datetime": datetime.now()}), 404


@errorhandlers.app_errorhandler(500)
def error_500(error):
    return jsonify({"url": request.url,
                    "status": f'{error}',
                    "datetime": datetime.now()}), 500
#
#
# @errorhandlers.app_errorhandler(ValueError)
# def error_ValueError(error):
#     return jsonify({"url": request.url,
#                     "status": f'{error}',
#                     "datetime": datetime.now()}), ValueError
#
#
# @errorhandlers.app_errorhandler(TypeError)
# def error_TypeError(error):
#     return jsonify({"url": request.url,
#                     "status": f'{error}',
#                     "datetime": datetime.now()}), TypeError
#
#
# @errorhandlers.app_errorhandler(IndexError)
# def error_IndexError(error):
#     return jsonify({"url": request.url,
#                     "status": f'{error}',
#                     "datetime": datetime.now()}), IndexError
#
#
# @errorhandlers.app_errorhandler(AttributeError)
# def error_AttributeError(error):
#     return jsonify({"url": request.url,
#                     "status": f'{error}',
#                     "datetime": datetime.now()}), AttributeError
