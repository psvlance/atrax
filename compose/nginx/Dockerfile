FROM nginx:1.17.3-alpine

RUN apk --no-cache add curl

COPY compose/nginx/entrypoint /entrypoint
COPY compose/nginx/start /start

RUN sed -i 's/\r//' /entrypoint && chmod +x /entrypoint \
    && sed -i 's/\r//' /start && chmod +x /start

ENTRYPOINT ["/entrypoint"]
