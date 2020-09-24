from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length


class VMRequestForm(FlaskForm):
    username = StringField('username', [
        DataRequired()])
    #recaptcha = RecaptchaField()
    submit = SubmitField('Submit')