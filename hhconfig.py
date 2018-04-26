class Config:
    DEBUG = False

    # Business config
    url1 = 'https://api.hh.ru/vacancies?text={}&area=1&search_field=name&date_from={}&date_to={}&per_page=100&order_by=publication_time'
    url2 = 'https://api.hh.ru/vacancies?text={}&area=1&search_field=name&date_from={}&date_to={}&per_page=100&order_by=publication_time'
    url3 = 'https://api.hh.ru/vacancies?text={}&area=1&search_field=name&search_field=description&date_from={}&date_to={}&per_page=100&order_by=publication_time'
    # Matching urls to graphs
    urls = {1: url1, 2: url2, 3: url3}
    titles = {1: 'Профессии', 2: 'Языки программирования - в названии вакансии', 3: 'Языки программирования - в описании вакансии'}
    description = 'Число новых вакансий в день для каждого ключевого слова или предложения'
    head = 'данные hh.ru'
    largeGraphHeight = 580

    # SQLAlchemy config
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Scheduler config
    JOBS = [
        {
            'id': 'job1',
            'func': '__main__:get_hh_data',
            'trigger': 'interval',
            'days': 1
        }
    ]
