#!/bin/sh

DATE="$(date "+%Y%m%d%H%M")"
SERVICE_NAME="latonaio/get-robot-data-triggered-by-ui"
docker build -t ${SERVICE_NAME}:${DATE} .
docker tag ${SERVICE_NAME}:${DATE} ${SERVICE_NAME}:latest
