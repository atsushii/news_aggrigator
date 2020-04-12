from views import *
from models import *
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile("../config.py")

db = SQLAlchemy(app)
db.init_app(app)


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
