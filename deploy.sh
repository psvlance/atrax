#!/usr/bin/env bash

COMPOSE_HTTP_TIMEOUT=200
docker-compose -f docker-compose.yml -p atrax up --build
