from database.database import db


class Sandwichs (db.Model):
    id_s = db.Column(db.Integer, primary_key=True)
    nom_s = db.Column(db.Text)
    description = db.Column(db.Text)
    prix_s = db.Column(db.Integer)
    quantite_totale = db.Column(db.Integer)
    quantite_restante = db.Column(db.Integer)
    est_epuise = db.Column(db.Boolean)

class Reservation (db.Model):
    id_r = db.Column(db.Integer, primary_key=True)
    nom_client = db.Column(db.Text)
    prenom_client = db.Column(db.Text)
    nom_s = db.Column(db.Text)
    quantite_reservation = db.Column(db.Integer)

class Client (db.Model):
    id_c = db.Column(db.Integer, primary_key=True)
    nom_client = db.Column(db.Text)
    prenom_client = db.Column(db.Text)