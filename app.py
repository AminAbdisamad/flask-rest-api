from flask_restful import Api

from db import apps
from resources.product import ProductAPI, AddProduct, GetAllProducts
from resources.user import RegisterUser, GetUsers, Users


# init api
# app = Flask(__name__)
api = Api(apps)


# Product resources URL
api.add_resource(ProductAPI, '/product/<id>')
api.add_resource(AddProduct, '/product')
api.add_resource(GetAllProducts, '/products')

# User Resources URL
api.add_resource(RegisterUser, '/user')
api.add_resource(GetUsers, '/users')
api.add_resource(Users, '/user/<id>')


# run api
if __name__ == '__main__':
    apps.run(debug=True)
