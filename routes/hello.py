from flask import Flask, render_template, Blueprint
from flask_sse import sse

hello = Blueprint("hello", __name__)

@hello.route('/')
def publish_hello():
    sse.publish({"message": "Hello!"})
    return "Message sent!"