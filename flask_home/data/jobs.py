import datetime

import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    team_leader = sqlalchemy.Column(sqlalchemy.Integer,
                                    sqlalchemy.ForeignKey("users.id"))
    job = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    work_size_ = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    colladorators = sqlalchemy.Column(sqlalchemy.DateTime,
                                      default=datetime.datetime.now)
    start_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                   default=datetime.datetime.now)
    end_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                 default=datetime.datetime.now)
    is_finished = sqlalchemy.Column(sqlalchemy.Integer,
                                    primary_key=True, autoincrement=True)
    user = orm.relationship('User')
    jobs = orm.relationship("Jobs", back_populates='user')
