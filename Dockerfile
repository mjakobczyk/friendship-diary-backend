FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev &&\
    apt-get install bash

COPY ./requirements.txt /requirements.txt

WORKDIR /

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ "/bin/bash", "./start.sh"]
