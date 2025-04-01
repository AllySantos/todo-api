from flask import Flask
from routes.user_routes import bp_user

app = Flask(__name__)

# Setting blueprints
app.register_blueprint(bp_user, url_prefix='/user')