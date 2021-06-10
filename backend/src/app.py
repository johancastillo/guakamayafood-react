# Dependencies
from flask import Flask, request
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
    title = db.Column(db.String(70), unique = True)
    description = db.Column(db.String(100))

    def __init__(self, title, description):
        self.title = title
        self.description = description


# Create tables
db.create_all()

# Database Schema
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description')

# Instance Schema
product_schema = ProductSchema()
products_schema = ProductSchema(many = True)


# Endpoints
@app.route("/")
def home():
    return "<h1>Welcome to my API REST!</h1>"

@app.route("/api/products", methods = ['POST'])
def create_product():
    print(request.json)
    return "Hello"


app.run(port = 8080, debug = True, host = "0.0.0.0")

