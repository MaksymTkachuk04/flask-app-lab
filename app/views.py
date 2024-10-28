from flask import Blueprint, render_template, request, redirect, url_for
users_bp = Blueprint('users', __name__, url_prefix='/users')

@users_bp.route('/')
def main():
    return render_template("base.html")

@users_bp.route('/homepage') 
def home():
    """View for the Home page of your website."""
    agent = request.user_agent

    return render_template("home.html", agent=agent)

@users_bp.route('/hi/<string:name>')
def greetings(name):
    name = name.upper()
    age = request.args.get("age", None, int)
    return render_template("hi.html", name=name, age=age)

@users_bp.route('/admin')
def admin():
    to_url = url_for("users.greetings", name="administrator", age=45, _external=True)
    return redirect(to_url)