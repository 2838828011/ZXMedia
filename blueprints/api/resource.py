from flask import Blueprint, abort, send_file
from core.function.picture import get_pic as get_picture

bl = Blueprint('api_resource', __name__, url_prefix='/api/resource')


@bl.route('/pic/<picture_id>')
def get_pic(picture_id):
    if picture_id == '':
        return abort(404)
    else:
        path = get_picture(picture_id)
        if path is None:
            return abort(404)
        else:
            return send_file(path[0])
