FROM ubuntu:latest

RUN mkdir /setup_web
COPY ./0-setup_web_static_copy.sh /setup_web
WORKDIR /setup_web
RUN ./0-setup_web_static_copy.sh