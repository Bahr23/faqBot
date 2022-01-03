from models import *

with db_session:
    TOKEN = Settings.get(key='TOKEN').value