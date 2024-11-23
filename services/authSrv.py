import jwt
import datetime
import os
from repository.repoSQL import repoSQL
from middleware.hashPass import hash_password

class authSrv():
    def __init__(self):
        self.secret_key = os.getenv("SECRET_KEY")
        self.query_service = repoSQL('users', ['id', 'email', 'firstname', 'lastname', 'status'])

    def loginSrv(self, payload):
        if payload:
            email = payload["email"]
            password = hash_password(payload["password"])
            result = self.query_service.get_by_conditions({
                "email": email,
                "password": password
            })
            if result:
                token = jwt.encode({
                    "firstname": result[0]["firstname"],
                    "lastname": result[0]["lastname"],
                    "email": result[0]["email"],
                    "status": result[0]["status"],
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
                }, self.secret_key, algorithm="HS256")
                return token
