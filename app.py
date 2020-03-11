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
    S1 = Produits(nom_s="Sandwich Poulet",
                   categorie= "Sandwichs",
                   description="Pain au sesame, poulet, tomates ",
                   prix_s="2",
                   est_epuise=False)

    S2 = Produits(nom_s="Sandwich Thon",
                  categorie="Sandwichs",
                  description="Pain de seigle, thon, concombres, salade",
                  prix_s="2",
                  est_epuise=False)

    S3 = Produits(nom_s="Salade César",
                   categorie="Salades",
                   description="Blanc de poulet, parmesan, tomates",
                   prix_s="2",
                   est_epuise=False)

    S4 = Produits(nom_s="Wrap Poulet",
                  categorie="Wraps",
                  description="Blanc de poulet, avocats, salade",
                  prix_s="2",
                  est_epuise=False)

    S5 = Produits(nom_s="Pates au pesto",
                  categorie="PlatsChauds",
                  description="Pesto",
                  prix_s="2",
                  est_epuise=False)

    db.session.add(S1)
    db.session.add(S2)
    db.session.add(S3)
    db.session.add(S4)
    db.session.add(S5)

    ##########################################################################################
    #  CREATION BASE DE DONNEES CLIENT
    ##########################################################################################

    C1 = Client(nom_client="test",
                prenom_client="test")
    db.sessions.add(C1)
    db.session.commit()


##########################################################################################
# LIEN PAGES
##########################################################################################
@app.route('/accueil')
def afficher_accueil():

    categories_dict = {}
    categories1 = set([p.categorie for p in Produits.query.all()])

    for category_name in categories1:
        categories_dict[category_name] = Produits.query.filter_by(categorie=category_name).all()

    return flask.render_template("Accueil.html.jinja2", categories_dict=categories_dict)

@app.route('/')
def master():
    client = Client.query.filter_by(id_c=1).first()
    return flask.render_template("Master.html.jinja2", client=client)


@app.route('/reservation/<id>')
def reservation(id):
    produit_select = Produits.query.filter_by(id_s = id).first()
    client = Client.query.filter_by(id_c=1).first()
    return flask.render_template("Reservation.html.jinja2", produit=produit_select, client=client)

##########################################################################################
# LIEN PRODUITS
##########################################################################################
@app.route('/<cat>')
def produits(cat):
    #quantite_restante = Produits.query.filter_by(categorie=cat).count()

    list_produits=Produits.query.filter_by(categorie=cat).all()
    if len(list_produits) == 0:
        cat = cat + " sont épuisés"
    return flask.render_template("PageCardProduits.html.jinja2", sandwich_1=list_produits, categorie = cat)





##########################################################################################
# MAIN
##########################################################################################
if __name__ == '__main__':
    app.run()
