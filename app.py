import flask
from flask import Flask

#from database.database import db, init_database

app: Flask = Flask(__name__)

#db.init_app(app)                        # (1) flask prend en compte la base de donnee
#with app.test_request_context():         # (2) bloc execute a l'initialisation de Flask


#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/database.db"
#app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

@app.route('/accueil')
def afficher_accueil():
   return flask.render_template("Accueil.html.jinja2")

@app.route('/')
def master():
    return flask.render_template("Master.html.jinja2")

@app.route('/reservation')
def reservation(produit):
    return flask.render_template("Reservation.html.jinja2", produit=produit)





if __name__ == '__main__':
    app.run()
