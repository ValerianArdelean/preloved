from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
def setup_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://valerian@localhost:5432/preloved'
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
        db.session.commit(self)

    def update(self):
        db.session.commit()

    def delete():
        db.session.delete(self)
        db.session.commit(self)

    def sesion_close(self):
        db.session.close()

    def format(self):
        return jsonify({
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'pieces': self.pieces,
            'immage_link': self.immage_link
        })
