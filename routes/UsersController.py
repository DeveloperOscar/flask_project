from flask import Blueprint, redirect, render_template, flash, url_for
from models.Users import Users
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from utils.db import db

usersRoute = Blueprint('users', __name__, url_prefix="/user")


class UserForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    submit = SubmitField("Submit")


@usersRoute.route('/', methods=['GET'])
def index():
    users = Users.query.order_by(Users.data_added)
    return render_template('Users/index.html', users=users)

@usersRoute.route("/create",methods=['GET'])
def create():
    form = UserForm()
    return render_template("Users/create.html", form = form)

@usersRoute.route('/insert', methods=['POST'])
def insert():
    form = UserForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None:
            user = Users(name=form.name.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()
        flash("Usuario añadido con exito")
    return redirect(url_for('users.index'))

@usersRoute.route('/edit/<id>',methods=['GET'])
def edit(id):
    form = UserForm()
    user = Users.query.filter_by(id = id).first()
    form.name.data = user.name;
    form.email.data = user.email;
    return render_template('Users/edit.html', form=form , id = id)

@usersRoute.route('/update/<id>',methods=['POST'])
def update(id):
    form = UserForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(id = id).first()
        user.name = form.name.data
        user.email = form.email.data
        db.session.commit()
        flash("Se modificaron los datos del usuario con exito")
    return redirect(url_for('users.index'))

@usersRoute.route('/delete/<id>',methods=['POST'])
def delete(id):
    user = Users.query.filter_by(id = id).first()
    db.session.delete(user)
    db.session.commit();
    flash(f"Se elimino al usuario {user.name}")
    return redirect(url_for('users.index'))

