from flask_wtf import FlaskForm
from wtforms import PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from wtforms.fields import EmailField


class RegistrationUser(FlaskForm):
    surname = EmailField('Фамилия', validators=[DataRequired()])
    name = EmailField('Имя', validators=[DataRequired()])
    age = EmailField('Возраст', validators=[DataRequired()])
    position = EmailField('Должность', validators=[DataRequired()])
    speciality = EmailField('Специальность', validators=[DataRequired()])
    address = EmailField('Модуль', validators=[DataRequired()])
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')