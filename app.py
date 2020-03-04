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
    S1 = Sandwichs(nom_s="Sandwich au poulet",
                   description="pain sesame, poulet, tomates ",
                   prix_s="2",
                   quantite_totale=5,
                   quantite_restante=1,
                   est_epuise=False)
    S2 = Sandwichs(nom_s="Sandwich au thon",
                   description="pain sesame,thon, tomates ",
                   prix_s="2",
                   quantite_totale=5,
                   quantite_restante=5,
                   est_epuise=False)
    S3 = Sandwichs(nom_s="Sandwich au jambon",
                   description="pain sesame,jambon, tomates ",
                   prix_s="2",
                   quantite_totale=5,
                   quantite_restante=4,
                   est_epuise=False)
    db.session.add(S1)
    db.session.add(S2)
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

@app.route('/sandwichs')
def sandwichs():
    sandwichs_all = Sandwichs.query.all()
    return flask.render_template("Sandwichs.html.jinja2",sandwichs_1=sandwichs_all)

@app.route('/reservation')
def reservation():
    return flask.render_template("Reservation.html.jinja2")

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







##########################################################################################
# MAIN
##########################################################################################
if __name__ == '__main__':
    app.run()
