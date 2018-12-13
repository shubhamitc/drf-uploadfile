# Dockerfile

# FROM directive instructing base image to build upon
FROM python:3.7
#FROM eventhandler:v11


# COPY ppp-prod-0c56d039a18d.json /root/ppp-prod-0c56d039a18d.json
RUN apt-get update -qqy && apt-get install -qqy \
        curl \
        gcc \
        python-dev \
        python-setuptools \
        apt-transport-https \
        lsb-release \
        openssh-client \
        git \
        telnet \
        vim

ENV WORKDIR=/opt/drf
WORKDIR $WORKDIR
ADD . $WORKDIR

# Backup sh and put bash as primary shell
RUN mv /bin/sh /bin/sh.old  && ln -s /bin/bash /bin/sh 

RUN pip install -r requirements.txt && \
     python manage.py makemigrations && \
     python manage.py migrate


ENTRYPOINT exec python3.7 manage.py runserver 0.0.0.0:8000
EXPOSE 8000