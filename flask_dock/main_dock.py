import datetime

from flask import Flask, request, render_template, redirect, session, make_response
from flask_login import login_required, logout_user, login_user, LoginManager

from data import db_session, jobs_api
from data.add_jobs_form import AddJobsForm
from data.jobs import Jobs
from data.registration import RegistrarionUser
from data.users import User
from flask_dock.data.login_form import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(
    days=365
)
login_manager = LoginManager()
login_manager.init_app(app)


@app.route("/")
def index():
    db_session.global_init("db/jobs.db")
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    user = db_sess.query(User).all()
    return render_template("index.html", jobs=jobs, user=user)


@app.route("/cookie_test")
def cookie_test():
    visits_count = int(request.cookies.get("visits_count", 0))
    if visits_count:
        res = make_response(
            f"Вы пришли на эту страницу {visits_count + 1} раз")
        res.set_cookie("visits_count", str(visits_count + 1),
                       max_age=60 * 60 * 24 * 365 * 2)
    else:
        res = make_response(
            "Вы пришли на эту страницу в первый раз за последние 2 года")
        res.set_cookie("visits_count", '1',
                       max_age=60 * 60 * 24 * 365 * 2)
    return res


@app.route("/session_test")
def session_test():
    visits_count = session.get('visits_count', 0)
    session['visits_count'] = visits_count + 1
    return make_response(
        f"Вы пришли на эту страницу {visits_count + 1} раз")


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/addjobs', methods=['GET', 'POST'])
@login_required
def add_jobs():
    form = AddJobsForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        addjob = Jobs(
            team_leader=form.team_leader.data,
            job=form.job.data,
            work_size=form.work_size.data,
            collaborators=form.collaborators.data,
            is_finished=form.is_finished.data)
        db_sess.add(addjob)
        db_sess.commit()
        return redirect('/')
    return render_template('add_jobs.html', title='Добавление работы',
                           form=form)


@app.route('/register', methods=['GET', 'POST'])
def registration():
    form = RegistrarionUser()
    print(1)
    if form.validate_on_submit():
        print(2)
        if form.password.data != form.password_agin.data:
            return render_template('register.html', title='Регистрация пользователя',
                                   form=form, message='Пароли не совпадают')
        print(3)
        db_sess = db_session.create_session()
        print(4)
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация пользователя',
                                   form=form, message='Пользователь с данной почтой уже существует')
        print(5)
        user = User(
            surname=form.surname.data,
            name=form.name.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data, email=form.email.data)
        user.set_password(form.password.data)
        print(6)
        db_sess.add(user)
        print(7)
        db_sess.commit()
        login_user(user)
        return redirect('/')
    return render_template('register.html', title='Регистрация пользователя',
                           form=form)


def main():
    db_session.global_init("db/blogs.db")
    app.register_blueprint(jobs_api.blueprint)
    app.run()


if __name__ == '__main__':
    main()
