from flask import Blueprint, render_template

home = Blueprint('home', __name__, template_folder='app/templates/api')

class homeCtrl():

    @home.route('/')
    def Home():
        return render_template('api/api.html')
