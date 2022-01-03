from models import *


@db_session
def find_question(query):
    sqlq = ' '.join(f'{q} |' for q in query.split())[:-2]
    # sql = f"SELECT * FROM question WHERE to_tsvector('russian', \"question\")" \
    #     f" || to_tsvector('russian', answer) @@ to_tsquery('russian', '{sqlq}')"
    sql = f"SELECT * FROM question WHERE to_tsvector('russian', \"question\") @@" \
        f" to_tsquery('russian', '{sqlq}') LIMIT 10"
    rows = db.select(sql)
    return rows


@db_session
def get_question(id):
    question = Question.get(id=id)
    if question:
        text = f"<b>{question.question}</b>\n\n<i>{question.answer}</i>"
        return text
    else:
        return False


@db_session
def get_user_or_error(id):
    try:
        user = User.get(user_id=id)
        if not user.id:
            raise Exception
        return user
    except Exception:
        return False
