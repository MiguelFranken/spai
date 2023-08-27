#!/bin/sh

PORT=${PORT:-10000}

exec gunicorn -b 0.0.0.0:$PORT main:app
