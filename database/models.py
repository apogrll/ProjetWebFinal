from database.database import db

class Produits (db.Model):
    id_s = db.Column(db.Integer, primary_key=True)
    nom_s = db.Column(db.Text)
    categorie = db.Column(db.Text)
    description = db.Column(db.Text)
    prix_s = db.Column(db.Integer)
    quantite_restante = db.Column(db.Integer)
    est_epuise = db.Column(db.Boolean)
    prix_menu = db.Column(db.Integer)

class Client (db.Model):
    id_c = db.Column(db.Integer, primary_key=True)
    nom_client = db.Column(db.Text)
    prenom_client = db.Column(db.Text)

class Reservation (db.Model):
    id_r = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.Text)
    prenom = db.Column(db.Text)
    produit = db.Column(db.Text)