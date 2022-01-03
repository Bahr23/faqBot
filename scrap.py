from bs4 import BeautifulSoup
from requests import request
import csv
from models import *

with open('data.html', encoding='UTF-8') as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

questions = soup.find_all("a", class_="faqQ")

with db_session:
    for q in questions:
        question = q.text
        answer = soup.find('div', class_=f"faqA_{q.get('faqnum')}").text
        ques = Question(question=question, answer=answer)

