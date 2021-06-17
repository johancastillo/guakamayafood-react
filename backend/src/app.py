# Dependencies
from os import truncate
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from crypt import crypt
import hashlib


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


# **********
# * SHA256 *
# **********
class HASH:
    def hashGenerator(hash):
        digest = hash.hexdigest()
        return digest

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


class Session(db.Model):
    __tablename__ = "sessions"

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(200), unique = True, nullable = False)
    token = db.Column(db.String(200), unique = True)

    def __init__(self, email, token):
        self.email = email
        self.token = token




# Create tables
db.create_all()

# ********************
# * Database Schemas *
# ********************

class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'price', 'discount_price', 'stars', 'categorie', 'description')

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name', 'country', 'city', 'birthday')

class SessionSchema(ma.Schema):
    class Meta:
        fields = ('id', 'email', 'token')

# *******************
# * Instance Schema *
# *******************

product_schema = ProductSchema()
products_schema = ProductSchema(many = True)

session_schema = SessionSchema()
sessions_schema = SessionSchema(many = True)

user_schema = UserSchema()
users_schema = UserSchema(many = True)


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


# ***********************
# * Endpoints for users *
# ***********************
@app.route("/api/login", methods = ['POST'])
def login():
    email = request.json['email']
    password = request.json['password']
    
    binaryPassword = bytes(password, 'utf8')
    h = hashlib.new("sha256", binaryPassword)
    passwordHash = HASH.hashGenerator(h)


    # Filter user
    user = db.session.query(User).filter_by(email = "jcjohan2707@gmail.com").first()
    
    # Validates data of user
    password_validate = user.password == passwordHash
    email_validate = user.email == email
    
    # Response generate
    if password_validate and email_validate:
        token = crypt(user.username + user.password)
        

        response = token

    elif not password_validate:
        response = "Contraseña incorrecta"

    elif not email_validate:
        response = "Email incorrecto"

    else:
        response = "Ha ocuurido un error"


    return jsonify({'response': str(response)})



# ***********
# * Run app *
# ***********
app.run(port = 8080, debug = True, host = "0.0.0.0")

