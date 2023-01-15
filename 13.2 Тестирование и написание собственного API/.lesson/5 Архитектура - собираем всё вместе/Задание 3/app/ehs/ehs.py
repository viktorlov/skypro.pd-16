from datetime import datetime

from flask import Blueprint, jsonify, request

ehs = Blueprint('ehs', __name__)


@ehs.app_errorhandler(404)
def error_404(error):
    return jsonify({"url": request.url,
                    "status": f'{error}',
                    "datetime": datetime.now()}), 404
