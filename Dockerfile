FROM python:3.10.1-alpine3.15

WORKDIR /var/www/sample-project

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT [ "/bin/sh", "-c", "FLASK_ENV=$APP_ENV flask run -p $APP_PORT -h $APP_HOST" ]
