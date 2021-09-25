from dotenv import load_dotenv
from routes.tic_tac_toe import tic_tac_toe
from routes.test import test
from routes.hello import hello
from routes.parasite import parasite
from routes.asteroid import asteroid
from routes.stonks import stonks
from flask import Flask, jsonify
from flask_sse import sse

load_dotenv()

app = Flask(__name__)
app.config["REDIS_URL"] = "redis://127.0.0.1:6379"
app.register_blueprint(sse, url_prefix='/stream')
app.register_blueprint(tic_tac_toe, url_prefix="/tic-tac-toe")
app.register_blueprint(test, url_prefix="/test")
app.register_blueprint(hello, url_prefix="/hello")
app.register_blueprint(stonks, url_prefix="/stonks")
app.register_blueprint(parasite, url_prefix="/parasite")
app.register_blueprint(asteroid, url_prefix="/asteroid")

@app.route("/")
def index():
    data = { "first": 1 }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True) #debug true = change file will refresh the server
    #app.run(true)


