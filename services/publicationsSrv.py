from flask import request, flash, json
from config.db import pgsqlConn, sql
from repository.repoSQL import repoSQL

class publicationsSrv():
    def __init__(self):
        self.query_service = repoSQL('publicaciones', ['id', 'titulo', 'descripcion', 'descripcion_full', 'status'])

    def getAllSrv(self):
        return self.query_service.get_all()

    def getByIdSrv(self, id):
        return self.query_service.get_by_id(id)

    def postSrv(self, payload):
        if payload:
            pub_data = {
                "titulo": payload["titulo"],
                "descripcion": payload["descripcion"],
                "descripcion_full": payload["descripcion_full"]
            }
            if "id" in payload:
                pub_data["id"] = payload["id"]
            if "status" in payload:
                pub_data["status"] = payload["status"]

            result = self.query_service.insert(pub_data)
            if result:
                flash('Publicación agregada exitosamente')
            else:
                flash('Error al agregar la publicación')
            return result

    def putSrv(self, id, payload):
        if payload:
            pub_data = {
                "titulo": payload["titulo"],
                "descripcion": payload["descripcion"],
                "descripcion_full": payload["descripcion_full"],
                "status": payload["status"]
            }
            if "id" in payload:
                pub_data["id"] = payload["id"]
            if "status" in payload:
                pub_data["status"] = payload["status"]

            result = self.query_service.update(id, pub_data)
            if result:
                flash('Publicación actualizada exitosamente')
            else:
                flash('Error al actualizar la publicación')
            return result

    def deleteSrv(self, id):
        if id:
            result = self.query_service.delete(id)
            if result:
                flash('Publicación eliminado exitosamente')
            else:
                flash('Error al eliminado la publicación')
            return result