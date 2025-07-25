from flask import Flask, Blueprint, request, render_template, make_response, jsonify

blog_abtest = Blueprint("blog", __name__)


@blog_abtest.route("/set_email", methods=["GET"])
def set_email():
    print(request.args.get("user_email"))
    return make_response(jsonify(success=True), 200)


@blog_abtest.route("/test_blog")
def test_blog():
    return render_template("blog_A.html")
