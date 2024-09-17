from functools import wraps
from flask import request, jsonify, g
import jwt
import os

def authorize(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split()[1]

        if not token:
            return jsonify({"message": "no autorizado"}), 401

        try:
            secret_key = os.getenv("SECRET_KEY")
            data = jwt.decode(jwt=token, key=secret_key, algorithms=["HS256"])
            g.user = data
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "token expirado"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "token invalido"}), 401

        return f(*args, **kwargs)

    return decorated_function
