FROM node:10-jessie

COPY compose/frontend/entrypoint /entrypoint
COPY compose/frontend/start /start

RUN sed -i 's/\r//' /entrypoint && chmod +x /entrypoint \
    && sed -i 's/\r//' /entrypoint && chmod +x /start

COPY frontend /project
WORKDIR /project

RUN npm i

ENTRYPOINT ["/entrypoint"]