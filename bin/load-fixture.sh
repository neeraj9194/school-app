#!/usr/bin/env bash
docker-compose run web ./manage.py migrate
docker-compose run web ./manage.py loaddata fixture/student.json
docker-compose run web ./manage.py loaddata fixture/teacher.json
docker-compose run web ./manage.py loaddata fixture/auth.json
