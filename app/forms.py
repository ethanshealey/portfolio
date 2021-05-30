from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from wtforms.widgets import HiddenInput

class ContactForm(FlaskForm):
    name = StringField(validators=[DataRequired()])
    email = StringField(validators=[DataRequired(), Email()])
    message = TextAreaField(validators=[DataRequired()])
    submit = SubmitField()