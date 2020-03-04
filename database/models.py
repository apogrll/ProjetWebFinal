from database.database import db


class Produit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.Text)
    type = db.Column(db.Text)
    description = db.Column(db.Text)
    quantite_totale = db.Column(db.Integer)
    quantite_restante = db.Column(db.Integer)
    est_epuise = db.Column(db.Boolean)

