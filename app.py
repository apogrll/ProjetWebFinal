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
    #  CREATION BASE DE DONNEES PRODUITS
    ##########################################################################################
    S1 = Produits(nom_s="Sandwich au poulet",
                   categorie= "Sandwichs",
                   description="pain sesame, poulet, tomates ",
                   prix_s="2",
                   quantite_totale=5,
                   quantite_restante=1,
                   est_epuise=False)

    S2 = Produits(nom_s="Sandwich au pfbjndo",
                  categorie="Sandwichs",
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
    db.session.add(S2)
    db.session.add(S3)


    db.session.commit()


##########################################################################################
# LIEN PAGES
##########################################################################################
@app.route('/accueil')
def afficher_accueil():
    sandwichs_all = Produits.query.filter_by(categorie="Sandwichs").all()
    salades_all = Produits.query.filter_by(categorie="Salades").all()
    wraps_all = Produits.query.filter_by(categorie="Wraps").all()
    vegetariens_all = Produits.query.filter_by(categorie="Vegetariens").all()
    platschauds_all = Produits.query.filter_by(categorie="PlatsChauds").all()
    listes_produits=[sandwichs_all, salades_all, wraps_all, vegetariens_all, platschauds_all]
    return flask.render_template("Accueil.html.jinja2", listep=listes_produits)

@app.route('/')
def master():
    return flask.render_template("Master.html.jinja2")


@app.route('/reservation/<id>')
def reservation(id):
    produit_selct = Produits.query.filter_by(id_s = id).first()
    client = Client.query.filter_by(id_c=1).first()
    return flask.render_template("Reservation.html.jinja2", produit=produit_selct, client=client)

##########################################################################################
# LIEN PRODUITS
##########################################################################################
@app.route('/<cat>')
def produits(cat):
    list_produits=Produits.query.filter_by(categorie=cat).all()
    return flask.render_template("PageCardProduits.html.jinja2", sandwich_1=list_produits, categorie = cat)


@app.route('/Sandwichs')
def sandwichs():
    sandwichs_all = Produits.query.filter_by(categorie="Sandwichs").all()
    cat = "Sandwichs"
    return flask.render_template("PageCardProduits.html.jinja2",sandwichs_1=sandwichs_all, categorie=cat)

@app.route('/Salades')
def salades():
    salades_all = Produits.query.filter_by(categorie="Salades").all()
    return flask.render_template("PageCardProduits.html.jinja2",sandwichs_1 = salades_all)

@app.route('/Wraps')
def wraps():
    wraps_all = Produits.query.filter_by(categorie="Wraps").all()
    return flask.render_template("PageCardProduits.html.jinja2", sandwichs_1=wraps_all)

@app.route('/Vegetarien')
def vegetariens():
    vegetariens_all = Produits.query.filter_by(categorie="Vegetariens").all()
    return flask.render_template("PageCardProduits.html.jinja2", sandwichs_1=vegetariens_all)

@app.route('/Platschauds')
def platschauds():
    platschauds_all = Produits.query.filter_by(categorie="PlatsChauds").all()
    return flask.render_template("PageCardProduits.html.jinja2", sandwichs_1=platschauds_all, categorie=platschauds)







##########################################################################################
# MAIN
##########################################################################################
if __name__ == '__main__':
    app.run()
