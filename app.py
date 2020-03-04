import flask
from flask import Flask
from database.database import db
from database.models import *
app: Flask = Flask(__name__)

##########################################################################################
#  CREATION BASE DE DONNEES
##########################################################################################

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
with app.test_request_context():
    db.drop_all()
    db.create_all()

    S1 = Sandwichs(nom_s="sandwich au poulet",
                   description="pain sesame , poulet, tomates ",
                   prix_s="2",
                   quantite_totale=5,
                   quantite_restante=1,
                   est_epuise=False)

    S2 = Sandwichs(nom_s="sandwich au thon",
                   description="pain sesame ,thon, tomates ",
                   prix_s="2",
                   quantite_totale=5,
                   quantite_restante=1,
                   est_epuise=False)

    db.session.add(S1)
    db.session.add(S2)

    C1 = Client(nom_client='Fourneau',
                 prenom_client='Elsa')

    db.session.add(C1)

    db.session.commit()

##########################################################################################
# RECUPERATION BASE DE DONNEES
##########################################################################################

def recup_clients():
    return Client.query.all()

def recup_nom_sandwich():
    return Sandwichs.query.first().nom_s

def get_liste_sandwichs():
    nom = recup_nom_sandwich(sandwichs.noms_s)
    return nom



##########################################################################################
# PAGES
##########################################################################################

@app.route('/accueil')
def afficher_accueil():
   return flask.render_template("Accueil.html.jinja2")

@app.route('/')
def master():
    return flask.render_template("Master.html.jinja2")

@app.route('/reservation/<id_s>')
def reservation(id_s):
    sandwich = Sandwichs.query.filter_by(id_s = id_s).first()
    return flask.render_template("Reservation.html.jinja2", sandwich=sandwich)

@app.route('/wraps')
def wraps():
    return flask.render_template("Wraps.html.jinja2")

@app.route('/salade')
def salades():
    return flask.render_template("Salades.html.jinja2")
@app.route('/vegetarien')
def vegetariens():
    return flask.render_template("Vegetariens.html.jinja2")

@app.route('/platschauds')
def platschauds():
    return flask.render_template("PlatsChauds.html.jinja2")

@app.route('/sandwichs')
def sandwichs():
    sandwichs_all = Sandwichs.query.all()
    return flask.render_template("Sandwichs.html.jinja2", sandwichs_1=sandwichs_all)





##########################################################################################
# MAIN
##########################################################################################
if __name__ == '__main__':
    app.run()
