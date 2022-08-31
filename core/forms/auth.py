from flask_wtf import FlaskForm, RecaptchaField, Form
from wtforms import StringField, SubmitField, PasswordField, BooleanField, TextAreaField, FloatField
from wtforms.validators import DataRequired, Length, Email, NumberRange
from wtforms.fields import EmailField, IntegerField, TimeField, DateField, SelectField, DateTimeField

class LogInForm(FlaskForm):
    email = EmailField('email', validators=[DataRequired(), Length(3, 320)])
    password = PasswordField('password', validators=[DataRequired(), Length(3, 320)])

class SignUpForm(FlaskForm):
    email = EmailField('email', validators=[DataRequired(), Length(3, 320)])
    password1 = PasswordField('password1', validators=[DataRequired(), Length(3, 320)])
    password2 = PasswordField('password2', validators=[DataRequired(), Length(3, 320)])