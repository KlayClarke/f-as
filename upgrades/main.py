import csv
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms.validators import DataRequired
from flask import Flask, render_template, request
from wtforms import StringField, SubmitField, SelectField, URLField


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = URLField('Cafe location on Google Maps (URL)', validators=[DataRequired()])
    open = StringField('Opening time e.g, 5AM', validators=[DataRequired()])
    close = StringField('Closing time e.g, 530PM', validators=[DataRequired()])
    coffee = SelectField('Coffee Rating', validators=[DataRequired()], choices=['☕', '☕☕', '☕☕☕', '☕☕☕☕', '☕☕☕☕☕'])
    wifi = SelectField('Wifi Strength Rating', validators=[DataRequired()],
                       choices=['✘', '💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪'])
    power = SelectField('Power Outlet Strength Rating', validators=[DataRequired()],
                        choices=['✘', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    form.validate_on_submit()
    if request.method == 'POST' and form.validate_on_submit():
        location_addition = form.cafe.data, form.location.data, form.open.data, \
                            form.close.data, form.coffee.data, form.wifi.data, form.power.data
        with open('cafe-data.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(location_addition)
        return render_template('cafes.html')
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
