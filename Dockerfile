FROM python:3.12.0a4-alpine3.17

RUN mkdir /automation

COPY . /automation
COPY ./setup.py /automation

WORKDIR /automation

RUN python3 setup.py install

