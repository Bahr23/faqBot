from pony.orm import *
import os
import re
from urllib.parse import urlparse

db = Database()

# db.bind(provider='postgres', user='postgres', password='', host='localhost', database='')

db_url = urlparse(os.environ['DATABASE_URL'])
args = re.split('[:@]', db_url.netloc)
db.bind(provider=db_url.scheme, user=args[0], password=args[1], host=args[2], port=args[3], database=db_url.path[1:])


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