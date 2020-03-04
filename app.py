import flask
from flask import Flask

#from database.database import db, init_database
from database.database import db
from database.models import *

app: Flask = Flask(__name__)

#db.init_app(app)                        # (1) flask prend en compte la base de donnee
#with app.test_request_context():         # (2) bloc execute a l'initialisation de Flask

##########################################################################################
# BASE DE DONNEES
##########################################################################################

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db.init_app(app) # (1) flask prend en compte la base de donnee
with app.test_request_context(): # (2) bloc execute a l'initialisation de Flask
    db.create_all()

    S1 = Produit(id=1, nom="poulet", type="sandwich", description="poulet", quantite_totale=5, quantite_restante=1,
                 est_epuise=False)

    db.session.add(S1)
    db.session.commit()

##########################################################################################
# PAGES
##########################################################################################

@app.route('/accueil')
def afficher_accueil():
   return flask.render_template("Accueil.html.jinja2")

@app.route('/')
def master():
    return flask.render_template("Master.html.jinja2")

@app.route('/reservation')
def reservation():
    return flask.render_template("Reservation.html.jinja2")

@app.route('/sandwichs')
def sandwichs():
    return flask.render_template("Sandwichs.html.jinja2")


@app.route('/salades')
def salades():
    return flask.render_template("Salades.html.jinja2")

@app.route('/wraps')
def wraps():
    return flask.render_template("Wraps.html.jinja2")

@app.route('/vegetariens')
def vegetariens():
    return flask.render_template("Vegetariens.html.jinja2")

@app.route('/platschauds')
def platschauds():
    return flask.render_template("PlatsChauds.html.jinja2")


##########################################################################################
# MAIN
##########################################################################################
if __name__ == '__main__':
    app.run()
