from . import bp
from flask import render_template, redirect, request, url_for, make_response, session, flash
from datetime import timedelta

VALID_USERNAME = "user"
VALID_PASSWORD = "pass"

@bp.route("/profile")
def get_profile():
    if "username" not in session:
        flash("Invalid: Session.", "danger")
        return redirect(url_for("user_name.login"))
    cookies = request.cookies
    theme = request.cookies.get('theme', 'light')  # Світла тема за замовчуванням
    return render_template("profile.html", username=session["username"], cookies=cookies, theme=theme)

@bp.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form.get("login")
        password = request.form.get("password")
        
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            session["username"] = username
            flash("Success: session added successfully.", "success")
            return redirect(url_for("user_name.get_profile"))
        else:
            flash("Incorrect data! Please try again.", "danger")
            return redirect(url_for("user_name.login"))
            
    return render_template("login.html")

@bp.route('/logout')
def logout():
    session.pop('username', None)
    flash("You have successfully logged out.", "info")
    return redirect(url_for('user_name.login'))

# Додавання куків
@bp.route('/add_cookie', methods=['POST'])
def add_cookie():
    key = request.form.get('cookie_key')
    value = request.form.get('cookie_value')
    duration = int(request.form.get('cookie_duration', 60))  # тривалість за замовчуванням - 60 секунд
    response = make_response(redirect(url_for('user_name.get_profile')))
    response.set_cookie(key, value, max_age=duration)
    flash("Cookie added successfully!", "success")
    return response

# Видалення конкретного кукі
@bp.route('/delete_cookie', methods=['POST'])
def delete_cookie():
    key = request.form.get('delete_cookie_key')
    response = make_response(redirect(url_for('user_name.get_profile')))
    response.set_cookie(key, '', expires=0)
    flash("Cookie deleted!", "info")
    return response

# Видалення всіх куків
@bp.route('/delete_all_cookies', methods=['POST'])
def delete_all_cookies():
    response = make_response(redirect(url_for('user_name.get_profile')))
    for key in request.cookies.keys():
        response.set_cookie(key, '', expires=0)
    flash("Всі кукі видалено!", "info")
    return response

# Вибір кольорової схеми
@bp.route('/set_theme/<theme>')
def set_theme(theme):
    response = make_response(redirect(url_for('user_name.get_profile')))
    response.set_cookie('theme', theme, max_age=24*60*60)  # Зберігаємо тему на добу
    return response
