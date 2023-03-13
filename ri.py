from flask_login import LoginManager
from datetime import datetime
from flask import Flask, url_for, request


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class User(SqlAlchemyBase, UserMixin):
    __tablename__ = "users"
