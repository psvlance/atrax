import os


class Settings:
    DATABASE_URL = os.getenv('DATABASE', 'mongodb://mongo:27017/')
    APP_ID = os.getenv('APP_ID', '9766674221184b9a869dc0a46134cec5')

    DEBUG = bool(os.getenv('DEBUG', False))

    FLASK_ENV = os.getenv('FLASK_ENV', 'production')

    CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', '')
    CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND', '')


SETTINGS = Settings()
