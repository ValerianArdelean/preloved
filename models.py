from flask_sqlalchemy import SQLAlchemy
import os


db_path = os.environ['DATABASE_URL']



db = SQLAlchemy()
def setup_db(app, db_path=db_path):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.app = app
    db.init_app(app)


class Clothes(db.Model):
    __tablename__ = 'clothes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    price = db.Column(db.Integer)
    pieces = db.Column(db.Integer)
    immage_link = db.Column(db.String())

    def __repr__ (self):
        return f'{self.id} {self.name} {self.price} {self.pieces} {self.immage_link}'

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def sesion_close(self):
        db.session.close()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'pieces': self.pieces,
            'immage_link': self.immage_link
        }
