from flask import Flask
from routes.user_routes import bp_user
from routes.login_routes import bp_login
from routes.task_routes import bp_todo

app = Flask(__name__)

# Setting blueprints
app.register_blueprint(bp_user, url_prefix='/user')
app.register_blueprint(bp_login, url_prefix='/login')
app.register_blueprint(bp_todo, url_prefix='/todo')
