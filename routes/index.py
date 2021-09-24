from flask import request, jsonify, Blueprint 

index = Blueprint("index", __name__)

@index.route("/")
def home():
    data = { "first": 1 }
    return jsonify(data)