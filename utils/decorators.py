from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from flask import jsonify

from functools import wraps
from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request
from flask import jsonify

def manager_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        current_user = get_jwt_identity()
        if current_user['role'] != 'manager':
            return jsonify({"msg": "Managers only!"}), 403
        return fn(*args, **kwargs)
    return wrapper


def staff_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()
        if claims['sub']['role'] not in ['staff', 'manager']:
            return jsonify({'msg': 'Staff only!'}), 403
        return fn(*args, **kwargs)
    return wrapper
