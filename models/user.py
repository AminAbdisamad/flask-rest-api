from db import db, mm


class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    @classmethod
    def findUserByUsername(cls, username):
        username = cls.query.filter_by(username=username).first()
        return username

    @classmethod
    def findUserById(cls, id):
        userId = cls.query.filter_by(id=id).first()
        return userId


# Product Schema
class UserSchema(mm.Schema):
    class Meta:
        fields = ('id', 'username', 'password')


# db.create_all()
