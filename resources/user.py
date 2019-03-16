from flask import request, jsonify
from flask_restful import Resource
from db import db
from models.user import UserModel, UserSchema
from werkzeug.security import generate_password_hash, check_password_hash

# userSchema
user_schema = UserSchema(strict=True)
users_schema = UserSchema(many=True, strict=True)


class RegisterUser(Resource):
    # Registering Users
    def post(self):

        username = request.json['username']
        hashedPassword = generate_password_hash(
            request.json['password'], method="sha256")
        userExist = UserModel.findUserByUsername(username)
        if userExist:
            return ({"message": "User already registered"})
        newUser = UserModel(username, hashedPassword)
        if newUser:
            db.session.add(newUser)
            db.session.commit()
            return user_schema.jsonify(newUser)
        return ({"message": "User could not be registered"})


class GetUsers(Resource):
    # Get all the Users
    def get(self):
        users = UserModel.query.all()
        result = users_schema.dump(users)
        return jsonify(result.data)


class Users(Resource):
    def get(self, id):
        id = UserModel.query.get(id)
        if id:
            return user_schema.jsonify(id)
        return ({"message": "user not found"}), 404

    def delete(self, id):
        id = UserModel.query.get(id)
        if id:
            db.session.delete(id)
            db.session.commit()
            return ({"message": "User Deleted Successfully"})
        return ({"message": "User couldn't found"})

    def put(self, id):
        id = UserModel.query.get(id)
        username = request.json['username']
        password = request.json['password']
        if id:
            id.username = username
            id.password = password
            db.session.commit()
            return user_schema.jsonify(id)
        return ({"message": "User does not exist"})
