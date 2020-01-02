FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev &&\
    apt-get install bash &&\
    apt-get install -y libpq-dev python3-dev

COPY ./requirements.txt /requirements.txt

WORKDIR /

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ENV FLASK_APP startup.py
ENV FLASK_DEBUG 1
ENV APP_CONFIG_FILE config.py
ENV TESTING True
ENV SECRET_KEY secret_key
ENV DB_TYPE postgres
ENV DB_USER postgres
ENV DB_PASSWORD password
ENV DB_HOSTNAME database
ENV DB_PORT 5432
ENV DB_NAME postgres
ENV SQLALCHEMY_DATABASE_URI None
ENV SQLALCHEMY_TRACK_MODIFICATIONS False

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ "/bin/bash", "./start.sh"]
