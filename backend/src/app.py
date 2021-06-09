from flask import Flask


app = Flask(__name__)

@app.route("/")
def Home():
    return "<h1>Hellooo World!</h1>"


app.run(port = 8080, debug = True, host = "0.0.0.0")

