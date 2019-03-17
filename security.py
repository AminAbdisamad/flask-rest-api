from flask_jwt import JWT, jwt_required
from werkzeug.security import check_password_hash
from models.user import UserModel
from db import apps

# auth
# userNameMapping = {x.username: x for x in users}
# userIdMapping = {x.id: x for x in users}
# git rm -rf --cached .


# Authenticate User
def authenticate(username, password):
    # user = userNameMapping.get(username, None)
    user = UserModel.findUserByUsername(username)
    if user and check_password_hash(user.password, password):
        return user


# identity
def identity(payload):
    userId = payload['identity']
    # return userIdMapping.get(userId, None)
    return UserModel.findUserById(userId)


apps.secret_key = "thisisthesecret"
jwt = JWT(apps, authenticate, identity)  # auth

# request = {}
# User = 'suer'
# passw = "pas"
# make_response = ''


# def login():

#     auth = request.authorization
#     if not auth or not auth.User or not auth.passw:
#         return make_response('could not verify', 401, {"WWW-Authenticate": 'basic realm="login required!"'})
#     User = UserModel.findUserByUsername("username")
#     if not User:
#         return ({"message": "No user Found"})
