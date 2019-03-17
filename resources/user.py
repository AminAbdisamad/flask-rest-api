from flask import request, jsonify
from flask_restful import Resource
from models.user import UserModel, UserSchema
from werkzeug.security import generate_password_hash
from security import jwt_required

# userSchema
user_schema = UserSchema(strict=True)
users_schema = UserSchema(many=True, strict=True)


class RegisterUser(Resource):
    # Registering Users
    @jwt_required()
    def post(self):
        username = request.json['username']
        hashedPassword = generate_password_hash(
            request.json['password'], method="sha256")
        userExist = UserModel.findUserByUsername(username)
        if userExist:
            return ({"message": "User already registered"})
        newUser = UserModel(username, hashedPassword)
        if newUser:
            UserModel.save(newUser)
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

    # @jwt_required
    def delete(self, id):
        userId = UserModel.query.get(id)
        if userId:
            UserModel.delete(userId)
            return ({"message": "User Deleted Successfully"})
        return ({"message": "User couldn't found"})

    # @jwt_required
    def put(self, id):
        updateUser = UserModel.query.get(id)
        username = request.json['username']
        hashedPassword = generate_password_hash(
            request.json['password'], method="sha256")

        if updateUser:
            updateUser.username = username
            updateUser.password = hashedPassword
            UserModel.update(updateUser)
            return user_schema.jsonify(updateUser)
        return ({"message": "User does not exist"})


# class Login(Resource):
#     username = request.json['username']
#     password = request.json['password']
