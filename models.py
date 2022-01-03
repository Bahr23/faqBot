from pony.orm import *

db = Database()

db.bind(provider='postgres', user='postgres', password='Tiraspol_2003', host='localhost', database='domain4ik')


class User(db.Entity):
    id = PrimaryKey(int, auto=True)
    user_id = Required(int)
    status = Required(str)
    username = Required(str)
    name = Optional(str)


class Question(db.Entity):
    id = PrimaryKey(int, auto=True)
    question = Required(str)
    answer = Required(str)


class Settings(db.Entity):
    key = Required(str)
    value = Required(str)


db.generate_mapping(create_tables=True)