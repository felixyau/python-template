import requests
from flask import request, jsonify, Blueprint 

test = Blueprint("test", __name__)

#function name cant be same as blueprint
@test.route("/", methods=["GET", "POST"])
def testdata():
    data = {"test":"testing"}
    return jsonify(data)