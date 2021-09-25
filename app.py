from dotenv import load_dotenv
from routes.encryption import encryption
from flask import Flask, jsonify

load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
    data = { "first": 1 }
    return jsonify(data)

app.register_blueprint(encryption, url_prefix="/")

if __name__ == "__main__":
    app.run() #debug true = change file will refresh the server
    #app.run(true)
