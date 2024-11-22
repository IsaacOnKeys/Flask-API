import json

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS=(app)
@app.route("/")
def hello_world():
    return "Hello World"

products = [
    {'id' : 143, 'name' : 'Notebook', 'price' : 5.49},
    {'id' : 144, 'name' : 'Black Marker', 'price' : 1.99}
]

# SIDE NOTE:
# To fetch data on products page:
# curl -X 'GET' 'http://127.0.0.1:5000/products' -H 'accept: application/json'

@app.route("/products", methods=['GET'])
def get_products():
    """GET: all products"""
    return jsonify(products)

@app.route("/products", methods=['GET'])
def get_product(id):
    """GET single product by ID"""
    for product in products:
        if product['id'] == id:
            return product
    return {"error": f"product with id {id} does not exist"}, 404

@app.route('/products', methods=['POST'])
def add_product(id, name, price):
    """POST: add product to products"""
    # NON API implementation
    # id = str(id)
    # name = str(name)
    # price = str(price)
    # new_product = {'id': id, 'name': name, 'price': price}
    # return products.append(new_product)
    products.append(request.get_json())
    # returns a tuple:
    return '', 201

@app.route("/products", methods=["PUT"])
def update_product(id):
    updated_product = json.loads(request.data)
    try:
        product = [p for p in products if products["id"] == id][0]
    except IndexError:
        return {"Error": "Item with id {} not found"}, 404
    for key, value in updated_product.items():
        product[key] = value
    return {"Success" : f"product with id {id} updated"}, 204

@app.route("/products", methods=["DELETE"])
def delete_product(id):
    id = int(id)
    try:
        product = [p for p in products if products["id"] == id][0]
    except IndexError:
        return {"Error": "Item with id {} not found"}, 404
    products.remove(product)
    return { "Success!" : "product with id {is} was removed." }, 204


if __name__=="__main__":
    app.run(debug=True)
    # When no port is specified, starts at default port 5000
