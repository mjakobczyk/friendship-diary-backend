FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev &&\
    apt-get install bash

COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ "/bin/bash", "./start.sh"]
