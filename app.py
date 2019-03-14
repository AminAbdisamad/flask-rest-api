import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Resource, reqparse, Api

# init api
app = Flask(__name__)
api = Api(app)

# Setup basedir
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'db.sql')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# init MM & alchemy
mm = Marshmallow(app)
db = SQLAlchemy(app)


# Products Model
class Product(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(300))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

    def __init__(self, name, description, price, qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty


# Product Schema
class ProductSchema(mm.Schema):
    class Meta:
        fields = ('_id', 'name', 'description', 'price', 'qty')


# init schema
product_schema = ProductSchema(strict=True)
product_schemas = ProductSchema(many=True, strict=True)

# Access resources
# api.add_resource(_, '/register')


# Add product
class ProductAPI(Resource):
    def get(self, id):
        product = Product.query.get(id)
        if product:
            return product_schema.jsonify(product)
        return ({"Message": "Product Not found"}), 404

    # Update product
    def put(self, id):
        product = Product.query.get(id)
        name = request.json['name']
        description = request.json['description']
        price = request.json['price']
        qty = request.json['qty']
        # Updating product with id
        product.name = name
        product.description = description
        product.price = price
        product.qty = qty
        # commiting to db
        db.session.commit()
        return product_schema.jsonify(product)

    # Delete Product
    def delete(self, id):
        product = Product.query.get(id)
        if product:
            db.session.delete(product)
            db.session.commit()
            return jsonify({"message": "Product deleted sucessfully"})
        return ({"message": "Product doesnt Exist"}), 404


class GetAllProducts(Resource):
    # get all products
    def get(self):
        getProducts = Product.query.all()
        result = product_schemas.dump(getProducts)
        return jsonify(result.data)


class AddProduct(Resource):
    def post(self):
        name = request.json['name']
        description = request.json['description']
        price = request.json['price']
        qty = request.json['qty']
        # adding product to the products class
        newProduct = Product(name, description, price, qty)
        # Adding product to db
        db.session.add(newProduct)
        db.session.commit()
        return product_schema.jsonify(newProduct)


api.add_resource(ProductAPI, '/product/<id>')
api.add_resource(AddProduct, '/product')
api.add_resource(GetAllProducts, '/products/')
# run api
if __name__ == '__main__':
    app.run(debug=True)
