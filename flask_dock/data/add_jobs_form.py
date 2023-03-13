from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class AddJobsForm(FlaskForm):
    team_leader = IntegerField('Id командира', validators=[DataRequired()])
    job = StringField('Название работы', validators=[DataRequired()])
    work_size = IntegerField("Время выполнения", validators=[DataRequired()])
    collaborators = StringField('Состав выполняющих работу', validators=[DataRequired()])
    is_finished = BooleanField("Работа завершена?")
    submit = SubmitField('Добавить')
