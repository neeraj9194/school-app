FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app

RUN apt update
RUN apt install pipenv -y

COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv install --system

COPY . /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver"]



