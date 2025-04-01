from flask import Flask
from routes.user_routes import bp_user
from routes.login_routes import bp_login

app = Flask(__name__)

# Setting blueprints
app.register_blueprint(bp_user, url_prefix='/user')
app.register_blueprint(bp_login, url_prefix='/login')
