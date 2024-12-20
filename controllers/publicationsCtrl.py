from flask import Blueprint, request, jsonify
from middleware.verifyAuth import authorize
from services.publicationsSrv import publicationsSrv

publications = Blueprint('publications', __name__)

class publicationsCtrl():
    @publications.route('/api/publications/get', methods=['GET'])
    @authorize
    def getAll():
        return jsonify(publicationsSrv().getAllSrv())

    @publications.route('/api/publications/get/<int:id>', methods=['GET'])
    @authorize
    def getById(id):
        return jsonify(publicationsSrv().getByIdSrv(id))

    @publications.route('/api/publications/post', methods=['POST'])
    @authorize
    def post():
        data = request.get_json()
        payload = { "title": data.get("title"), "description": data.get("description"), "description_full": data.get("description_full") }
        save = publicationsSrv().postSrv(payload)
        if save:
            return jsonify(save), 201
        else:
            return jsonify(save), 500

    @publications.route('/api/publications/put/<int:id>', methods=['PUT'])
    @authorize
    def put(id):
        data = request.get_json()
        payload = { "title": data.get("title"), "description": data.get("description"), "description_full": data.get("description_full"), "status": data.get("status") }
        save = publicationsSrv().putSrv(id, payload)
        if save:
            return jsonify(save), 200
        else:
            return jsonify(save), 500

    @publications.route('/api/publications/delete/<int:id>', methods=['DELETE'])
    @authorize
    def delete(id):
        save = publicationsSrv().deleteSrv(id)
        if save:
            return jsonify(save), 200
        else:
            return jsonify(save), 500