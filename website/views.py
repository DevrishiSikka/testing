from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user, login_user
from .models import *

views = Blueprint('views', __name__)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
loginned = True

@views.route('/')
def homepage():
    return render_template("homepage.html", user=current_user)


@views.route('/about')
def about():
    return render_template("about.html", user=current_user)


@views.route("/find")
@login_required
def find_roomie():
    return "<h1>here is roomie</h1>"


@views.route("/profile", methods=["POST", "GET"])
def profile():
    if request.method == "POST":
        print(request.form)
    return render_template("profile.html")


@views.route("/info", methods=["POST", "GET"])
def additional_info():
    if current_user.is_authenticated:
        return redirect(url_for('views.find_roomie'))
    else:
        if request.method == "POST":
            f_name = request.form.get('f_name')
            l_name = request.form.get('l_name')
            addr = request.form.get('addr')
            city = request.form.get('city')
            state = request.form.get('state')
            zip = request.form.get('zip')
            country = request.form.get('country')
            college_name = request.form.get('college_name')
            course = request.form.get('course')
            branch = request.form.get('branch')
            year = request.form.get('year')
            new_user_info = GeneralInfo(f_name=f_name, l_name=l_name, address=addr, city=city, state=state, zip=zip,
                                        country=country, college=college_name, course=course, branch=branch, year=year)
            db.session.add(new_user_info)
            db.session.commit()
            login_user(new_user_info, remember=True)

            return redirect(url_for('auth.login'))
    return render_template('dashboard.html')
