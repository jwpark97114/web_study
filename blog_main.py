from flask import Flask, jsonify, request, render_template, make_response
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from flask_cors import CORS
from blog_view import blog
from blog_control.user_mgmt import User
import os

# https only things can be tested with http
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"


app = Flask(__name__, static_url_path="/static")

CORS(app)


# For security should be changed to randomized key
# but will reset session data if the server restarts often
app.secret_key = "blog_server"

app.register_blueprint(blog.blog_abtest, url_prefix="/blog")

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = "strong"


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@login_manager.unauthorized_handler
def unauthorized():
    return make_response(jsonify(success=False), 401)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8080", debug=True)
