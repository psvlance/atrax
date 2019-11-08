FROM python:3.8-alpine

COPY backend/requirements.txt /requirements.txt
COPY compose/backend/entrypoint /entrypoint
COPY compose/backend/start /start
COPY compose/backend/start-celeryworker /start-celeryworker
COPY compose/backend/start-celerybeat /start-celerybeat
COPY compose/backend/start-celeryflower /start-celeryflower

RUN apk update && apk add --no-cache --virtual build-deps gcc python3-dev musl-dev postgresql-dev

RUN sed -i 's/\r//' /entrypoint && chmod +x /entrypoint \
    && sed -i 's/\r//' /start && chmod +x /start \
    && sed -i 's/\r//' /start-celeryworker && chmod +x /start-celeryworker \
    && sed -i 's/\r//' /start-celerybeat && chmod +x /start-celerybeat \
    && sed -i 's/\r//' /start-celeryflower && chmod +x /start-celeryflower \
    && pip install -r /requirements.txt && pip install gunicorn

COPY backend /project/backend
WORKDIR /project
ENTRYPOINT ["/entrypoint"]
