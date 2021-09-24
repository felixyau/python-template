from routes.encryption import encryption
from routes.index import index
from flask import Flask

app = Flask(__name__)
app.register_blueprint(encryption, url_prefix="/")
app.register_blueprint(index, url_prefix="/")

if __name__ == "__main__":
    app.run(debug=True, port=8000) #debug true = change file will refresh the server
