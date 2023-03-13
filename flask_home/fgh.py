from data import db_session
name = input()
db_session.global_init(f"db/{name}")
session = db_session.create_session()
for user in session.query(User).all:
    print(user)