from app import app
from dotenv import load_dotenv
import os
from controllers.homeCtrl import home
from controllers.publicationsCtrl import publications
from controllers.usersCtrl import users
from controllers.authCtrl import auth

app.register_blueprint(home)
app.register_blueprint(publications)
app.register_blueprint(users)
app.register_blueprint(auth)

# starting the app
PORT = os.getenv("PORT_APP")
if __name__ == "__main__":
    app.run(port=PORT, debug=True)
