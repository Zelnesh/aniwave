from flask import Flask, redirect, render_template, flash, url_for, request, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from api_request import RequestAPI
from animerate import AnimeRate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key'

class UrlForm(FlaskForm):
    """Form for Image APP generator"""
    url = StringField('Enter img tag from the following suggestion:wifu,neko,megumin,smile,nom,bite', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/imgapp', methods=['GET','POST'])
def img_app():
    url = None
    form = UrlForm()
    if request.method == 'POST':
        url = form.url.data
        prep_req = RequestAPI(url)
        req_result = prep_req.retrive_data()
        return render_template('img_app_result.html', data=req_result)
    return render_template('img_app.html', form=form)


@app.route('/radio')
def online_radio():
    return render_template('online_radio.html')

@app.route('/animerate')
def anime_rate():
    rate = AnimeRate()
    rate.get_data()
    return render_template('rate.html') 


if __name__ == '__main__':
    app.run(debug=True)
