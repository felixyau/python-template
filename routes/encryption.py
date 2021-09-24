from flask import request, jsonify, Blueprint 

encryption = Blueprint("encryption", __name__)

#function name cant be same as blueprint
@encryption.route("/encryption", methods=["POST"])
def encrypte():
    data = request.json
    return jsonify(data)
