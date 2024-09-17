from flask import Blueprint, request, jsonify, flash
from services.authSrv import authSrv

auth = Blueprint('auth', __name__)

class authCtrl():

    @auth.route('/api/auth/login', methods=['POST'])
    def login():
        data = request.get_json()
        payload = { "email": data.get("email"), "password": data.get("password") }
        response = authSrv().loginSrv(payload)
        if response:
            return jsonify(response), 200
        else:
            return jsonify(response), 401