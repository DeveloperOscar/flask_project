from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import  SQLAlchemy
from routes.UsersController import usersRoute

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqldb://root@127.0.0.1/Sistema"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = 'My super secret that no one is supposed to know'

SQLAlchemy(app)

class NamerForm(FlaskForm):
    name = StringField("Cual es tu nombre", validators=[DataRequired()])
    submit = SubmitField('Submit')

app.register_blueprint(usersRoute)

@app.route("/")
def index():
    name = "oscar"
    stuff = "This is bold text"
    flash("Welcome a flask web")
    return render_template("name.html", name=name,stuff=stuff)


#@app.route('/user/<name>')
#def user(name):
#    return render_template('user.html', name=name)

@app.route('/name', methods = ['GET','POST'])
def name():
    name = None
    form = NamerForm(request.form)
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Submit success")
    return render_template('user.html',name = name ,form = form)

#@app.route('/user/add', methods = ['GET','POST'])
#def add_user():
#    name = None
#    form = UserForm()
#    if form.validate_on_submit():
#        user = Users.query.filter_by(email = form.email.data).first()
#        if user is None:
#            user = Users(name = form.name.data, email = form.email.data)
#            db.session.add(user)
#            db.session.commit()
#        name = form.name.data
#        form.name.data = ''
#        form.email.data = ''
#        flash("Usuario añadido con exito")
#    our_users = Users.query.order_by(Users.data_added)
#    return render_template('add_user.html',
#            form = form,
#            name = name,
#            our_users= our_users)

