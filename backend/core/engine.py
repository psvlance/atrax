from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from celery import Celery
from celery.schedules import crontab

from werkzeug.debug import DebuggedApplication

from backend.apps import exchange
from backend.core.settings import SETTINGS


def get_initialized_app() -> Flask:
    """
    init flask`s app and return it
    """

    app = Flask(__name__)
    app.config.from_object(SETTINGS)
    app.url_map.strict_slashes = False
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    if app.debug:
        app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)

    return app


def get_initialized_celery(app: Flask) -> Celery:
    """
    init celery`s worker with flask`s settigns and return it
    """

    TASKS = (
        'backend.apps.tasks',
    )

    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'], include=TASKS)
    celery.conf.update(app.config)

    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask

    return celery


def register_tasks(app: Flask) -> None:
    """
    for a standalone container without flask`s app. Init each blank celery object with real data.
    For avoiding circular import imports should be in this local namespace not in a global namespace.
    each tasks file`s celery object should be here

    """

    from backend.apps.tasks import celery
    celery.conf.broker_url = app.config['CELERY_BROKER_URL']
    celery.conf.result_backend = app.config['CELERY_RESULT_BACKEND']


def register_rest(api: Api):
    """
    We will register all rest states here for convenient
    """

    exchange.register(api)


app = get_initialized_app()
celery = get_initialized_celery(app)
api = Api(app)
register_tasks(app)
register_rest(api)
