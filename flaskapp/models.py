from flaskapp import db


class LastDate(db.Model):
    __tablename__ = 'LastDate'
    published = db.Column(db.Date, primary_key=True, nullable=False)

    def __repr__(self):
        return '<LastDate %r>' % self.published


class HhRequest(db.Model):
    __tablename__ = 'Requests'
    sentence = db.Column(db.String(100), nullable=False)
    graph = db.Column(db.Integer, nullable=False)
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<HhRequest %r>' % ' '.join((self.sentence, str(self.graph)))


class Result(db.Model):
    __tablename__ = 'Results'
    published = db.Column(db.Date, nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    requestId = db.Column(db.Integer, db.ForeignKey('Requests.id'), nullable=False)
    count = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Result %r>' % ' '.join((str(self.requestId), str(self.count), str(self.published)))
