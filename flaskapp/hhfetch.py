from datetime import date, timedelta, datetime
import requests
import json
import urllib
import logging
from . import cnf
from .models import LastDate, HhRequest, Result, db


# Вспомогательная функция - получаем из БД стартовую дату
def get_last_date():
    return LastDate.query.first().published


# Вспомогательная функция - одиночный запрос на hh.ru
def make_request(text, for_date, graph):

    url = cnf.urls[graph].format(text, for_date, for_date)

    r = requests.get(url)
    parsed_string = json.loads(r.text)

    if 'errors' in parsed_string:
        logging.error('Bad response from hh.ru for date: ' + for_date)
        return None
    else:
        return parsed_string['found']


# Вспомогательная функция - получаем значения от hh.ru по всем параметрам за определенную дату
def fetch_for_single_date(date, values):
    for value in values:
        logging.info(value.sentence + ' ' + str(date))
        res = Result(published=date, requestId=value.id,
                     count=make_request(urllib.parse.quote(value.sentence), date, value.graph))
        db.session.add(res)


def fetch_hh():
    """
    Основная функция - получаем значения от hh.ru по всем датам от хранящейся в БД до вчерашней и коммитим
    """
    logging.info('Fetching time: ' + str(datetime.now()))
    fetch_values = HhRequest.query.all()

    day = timedelta(days=1)
    last_date = date.today() - day
    given_date = get_last_date()
    cursor_date = given_date + day

    while cursor_date <= last_date:
        fetch_for_single_date(cursor_date, fetch_values)
        cursor_date += day

    LastDate.query.update({'published': last_date})

    db.session.commit()
