import os

from celery import Celery
from celery.utils.log import get_task_logger
from celery.schedules import crontab

import requests
from flask_sqlalchemy import SQLAlchemy


DATABASE_URL = os.getenv('DATABASE', 'mongodb://mongo:27017/')
APP_ID = os.getenv('APP_ID', '9766674221184b9a869dc0a46134cec5')


log = get_task_logger(__name__)
celery = Celery()


def register_periodical_tasks(sender, **kwargs) -> None:
    sender.add_periodic_task(
        crontab(hour='*/24', minute=0),
        update_database.s(),
    )
celery.on_after_configure.connect(register_periodical_tasks)


class RegistryReader:
    URL = 'https://rossvyaz.ru/data/ABC-8xx.csv'

    def __init__(self):
        try:
            self.r = requests.get(self.URL, allow_redirects=True)
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
            self.r = None


    def __enter__(self):
        if self.r:
            return self
        raise

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __iter__(self):
        return self

    def __next__(self):





@celery.task
def update_database():
    pass