import flask

from . import db_session
from .jobs import Jobs
from main_dock import render_template

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict(only=('team_leader', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished'))
                 for item in jobs]
        }
    )
@blueprint.route('/api/jobs')
def get_jobs_id(job_id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).filter(Jobs.id == 1).first()
    if jobs:
        return jsonify(
            {
                'jobs':
                    [item.to_dict(only=('team_leader', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished'))
                     for item in jobs]
            }
        )
    else:
        return render_template('error.html', title='Error',
                               form=form, message='Даные не найдены')
    user = db_sess.query(User).filter(User.id == 1).first()
