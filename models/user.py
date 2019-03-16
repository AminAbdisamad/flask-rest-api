from db import db, mm


class UserModel(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def findUserByUsername(cls, username):
        username = cls.query.filter_by(username=username).first()
        return username

    @classmethod
    def findUserById(cls, _id):
        userId = cls.query.filter_by(_id=_id).first()
        return userId


# Product Schema
class UserSchema(mm.Schema):
    class Meta:
        fields = ('_id', 'username', 'password')


# db.create_all()
