import requests
from flask import request, jsonify, Blueprint, json
from sseclient import SSEClient

tic_tac_toe = Blueprint("tic_tac_toe", __name__)

#function name cant be same as blueprint
@tic_tac_toe.route("/", methods=["POST"])
def handle():
    battleId=""
    battleId = jsonify(request.get_json())["battleId"]
    url = 'https://cis2021-arena.herokuapp.com//tic-tac-toe/start/' + battleId
    init(url)
    # url = "http://127.0.0.1:5000/hello/"
    messages = SSEClient(url)
    print("msg", messages)
    for msg in messages:
        print(msg.data)
    return "hello"
    
def init(url):
    return requests.get(url).json()


