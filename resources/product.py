from flask import request, jsonify
from flask_restful import Resource
# from app import db

from models.product import Product, ProductSchema
from db import db
# init schema
product_schema = ProductSchema(strict=True)
product_schemas = ProductSchema(many=True, strict=True)


# This resource updates, deletes and gets specific product
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
