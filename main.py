import os
from flask_wtf import FlaskForm
from flask import Flask, render_template
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.secret_key = os.environ.get('FLASK_SECRET_KEY')


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
