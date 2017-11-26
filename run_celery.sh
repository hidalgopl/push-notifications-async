#!/usr/bin/env bash

sleep 10

su -m root -c "celery worker -A  settings.celery.app --loglevel=info"
