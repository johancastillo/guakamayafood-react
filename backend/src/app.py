# Dependencies
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Flask intance
app = Flask(__name__)

# Database parameters
enginedb = "mysql"         
driver = "pymysql"         
host = "localhost"         
user = "jcjohan"          
password = "password"    
database = "guakamayafood" 

# Database MySQL settings
app.config["SQLALCHEMY_DATABASE_URI"] = f"{enginedb}+{driver}://{user}:{password}@{host}/{database}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# ORM settings
db = SQLAlchemy(app)
ma = Marshmallow(app)

# *****************
# * Data Modeling *
# *****************

# Products table
class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(70), unique = True, nullable = False)
    image = db.Column(db.String(200), nullable = False)
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
    
    

# Categories table
class Categorie(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(70), unique = True)
    products_quantity = db.Column(db.Integer, default = 0)
    
    
    def __init__(self, title, products):
        self.title = title
        self.products = products

# Orders table
class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key = True)
    user = db.Column(db.String(70))
    products = db.Column(db.String(70))
    

    
    def __init__(self, user, products):
        self.user = user
        self.products = products


# Users table
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(70), unique = True)
    email = db.Column(db.String(70), unique = True)
    password = db.Column(db.String(200))
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

# ***************************
# * Endpoints  for products *
# ***************************

# Root route
@app.route("/")
def home():
    return render_template("index.html")

# Create product
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

# Get all products
@app.route("/api/products", methods = ["GET"])
def get_products():
    
    all_products = Product.query.all()
    result = products_schema.dump(all_products)

    return jsonify(result)


# Get single product
@app.route("/api/products/<id>", methods = ["GET"])
def single_product(id):
    product = Product.query.get(id)

    return product_schema.jsonify(product)

# Modificate single product
@app.route("/api/products/<id>", methods = ["PUT"])
def edit_product(id):
    # Get product
    product = Product.query.get(id)
    
    # Get data
    title = request.json["title"]
    price = request.json["price"]

    # Change values
    product.title = title
    product.price = price

    # Execute sentence
    db.session.commit()

    # Response
    return product_schema.jsonify(product)

# Delete one product
@app.route("/api/products/<id>", methods = ["DELETE"])
def delete_product(id):
    
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()

    return product_schema.jsonify(product)


# ***********
# * Run app *
# ***********
app.run(port = 8080, debug = True, host = "0.0.0.0")

