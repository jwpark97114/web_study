from flask import (
    Flask,
    Blueprint,
    request,
    render_template,
    make_response,
    jsonify,
    redirect,
    url_for,
    session,
)
from flask_login import login_user, current_user, logout_user
from blog_control.user_mgmt import User
import datetime
from blog_control.session_mgmt import BlogSession


blog_abtest = Blueprint("blog", __name__)


@blog_abtest.route("/set_email", methods=["GET", "POST"])
def set_email():

    if request.method == "GET":
        # print(request.args.get("user_email"))
        return make_response(jsonify(success=True), 200)
    else:
        # print("set_email", request.headers)

        # content type error
        # get_json requires the request content type to be application/json
        # check the html, its using form and therefore it should be request.form
        # print("set_email", request.form["user_email"])
        # print("blog_id", request.form["blog_id"])
        user = User.create(request.form["user_email"], request.form["blog_id"])
        login_user(user, remember=True, duration=datetime.timedelta(days=365))
        return redirect(url_for("blog.blog_fullstack"))


@blog_abtest.route("/logout")
def logout():
    User.delete(current_user.id)
    logout_user()
    return redirect(url_for("blog.blog_fullstack"))


@blog_abtest.route("/blog_fullstack")
def blog_fullstack():

    if current_user.is_authenticated:
        webpage_name = BlogSession.get_blog_page(current_user.blog_id)
        BlogSession.save_session_info(
            session["client_id"], current_user.user_email, webpage_name
        )
        return render_template(webpage_name, user_email=current_user.user_email)
    else:
        webpage_name = BlogSession.get_blog_page()
        BlogSession.save_session_info(session["client_id"], "anonymous", webpage_name)
        return render_template(webpage_name)
