import warnings
import subprocess
from flask_cors import CORS
from flask import Flask, jsonify, request, abort
import os
from models.db import db
from models.install import install_models
import os

warnings.filterwarnings("ignore")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db.init_app(app)
CORS(app)
 
with app.app_context():
    install_models()
    import routes

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", debug=True, port=port)
