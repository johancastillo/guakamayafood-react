# Dependencies
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Flask intance
app = Flask(__name__)

# Database parameter
host = "127.0.0.1"         
user = "someUser"          
passwd = "somePassword"    
database = "ucb-pvapp" 

# Database MySQL settings
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://jcjohan:password@localhost/guakamayafood"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# ORM settings
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Data Modeling
class Product(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(70), unique = True, nullable = False)
    price = db.Column(db.Float, default = 0)
    discount_price = db.Column(db.Float, default = 0)
    stars = db.Column(db.Integer, default = 0)
    categorie = db.Column(db.String(70))
    description = db.Column(db.String(100))

    def __init__(self, title, price, discount_price, stars, categorie, description,):
        self.title = title
        self.price = price
        self.discount_price = discount_price
        self.stars = stars
        self.categorie = categorie
        self.description = description


class Categorie(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(70), unique = True)
    products_quantity = db.Column(db.Integer, default = 0)
    
    
    def __init__(self, title, products):
        self.title = title
        self.products = products


class Order(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user = db.Column(db.String(70))
    products = db.Column(db.String(70))
    

    
    def __init__(self, user, products):
        self.user = user
        self.products = products


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(70), unique = True)
    first_name = db.Column(db.String(70))
    last_name = db.Column(db.String(70))
    country = db.Column(db.String(70))
    city = db.Column(db.String(70))
    addres = db.Column(db.String(70))
    birthday = db.Column(db.String(70))
    orders = db.Column(db.String(70))
    

    def __init__(self, user, products):
        self.user = user
        self.products = products




# Create tables
db.create_all()

# Database Schema
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'price', 'discount_price', 'stars', 'categorie', 'description')

# Instance Schema
product_schema = ProductSchema()
products_schema = ProductSchema(many = True)


# Endpoints
@app.route("/")
def home():
    return "<h1>Welcome to my API REST with Flask!</h1>"

@app.route("/api/products", methods = ['POST'])
def create_product():
    # print(request.json)

    title = request.json['title']
    price = request.json['price']
    discount_price = request.json['discount_price']
    stars = request.json['stars']
    categorie = request.json['categorie']
    description = request.json['description']

    new_product = Product(title, price, discount_price, stars, categorie, description)

    db.session.add(new_product)
    db.session.commit()

    return product_schema.jsonify(new_product)


@app.route("/api/products", methods = ["GET"])
def get_products():
    
    all_products = Product.query.all()
    result = products_schema.dump(all_products)

    return jsonify(result)


@app.route("/api/products/<id>", methods = ["GET"])
def single_product(id):

    return ""


# Run app
app.run(port = 8080, debug = True, host = "0.0.0.0")

