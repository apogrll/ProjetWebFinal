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

    ##########################################################################################
    #  CREATION BASE DE DONNEES SANDWICHS
    ##########################################################################################
    S1 = Produits(nom_s="Sandwich au poulet",
                   categorie= "Sandwichs",
                   description="pain sesame, poulet, tomates ",
                   prix_s="2",
                   quantite_totale=5,
                   quantite_restante=1,
                   est_epuise=False)

    S3 = Produits(nom_s="Salade 1",
                   categorie="Salades",
                   description="salade",
                   prix_s="2",
                   quantite_totale=5,
                   quantite_restante=4,
                   est_epuise=False)


    db.session.add(S1)
    db.session.add(S3)

    ##########################################################################################
    #  CREATION BASE DE DONNEES SALADES
    ##########################################################################################


    db.session.commit()



##########################################################################################
# LIEN PAGES
##########################################################################################
@app.route('/accueil')
def afficher_accueil():
   return flask.render_template("Accueil.html.jinja2")

@app.route('/')
def master():
    return flask.render_template("Master.html.jinja2")


@app.route('/reservation/<id_s>')
def reservation(id_s):
    #sandwich = Produits.query.filter_by(id_s = id_s).first()
    #client = Client.query.filter_by(id_c=1).first()
    return flask.render_template("Reservation.html.jinja2") #, sandwich=sandwich, client=client)

##########################################################################################
# LIEN PRODUITS
##########################################################################################
@app.route('/produits')
def produits():
    return flask.render_template("PageCardProduits.html.jinja2")


@app.route('/sandwichs')
def sandwichs():
    sandwichs_all = Produits.query.filter_by(categorie="Sandwichs").all()
    return flask.render_template("Sandwichs.html.jinja2",sandwichs_1=sandwichs_all)

@app.route('/salades')
def salades():
    salades_all = Produits.query.filter_by(categorie="Salades").all()
    return flask.render_template("PageCardProduits.html.jinja2",sandwichs_1 = salades_all)

@app.route('/wraps')
def wraps():
    wraps_all = Produits.query.filter_by(categorie="Wraps").all()
    return flask.render_template("PageCardProduits.html.jinja2", sandwichs_1=wraps_all)


@app.route('/vegetarien')
def vegetariens():
    vegetariens_all = Produits.query.filter_by(categorie="Vegetariens").all()
    return flask.render_template("PageCardProduits.html.jinja2", sandwichs_1=vegetariens_all)

@app.route('/platschauds')
def platschauds():
    platschauds_all = Produits.query.filter_by(categorie="PlatsChauds").all()
    return flask.render_template("PageCardProduits.html.jinja2", sandwichs_1=platschauds_all)







##########################################################################################
# MAIN
##########################################################################################
if __name__ == '__main__':
    app.run()
