from controller.book_controller import book_blueprint
from flask import Flask

app = Flask(__name__)
app.register_blueprint(book_blueprint)
