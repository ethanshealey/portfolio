from flask_wtf import FlaskForm
from wtforms import Form as NoCsrfForm, StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectMultipleField, IntegerField, FieldList, FormField
from wtforms.validators import DataRequired, Length
from wtforms.widgets import HiddenInput

class ContactForm(FlaskForm):
    name = StringField(validators=[DataRequired()])
    email = StringField(validators=[DataRequired()])
    message = TextAreaField(validators=[DataRequired()])
    submit = SubmitField()