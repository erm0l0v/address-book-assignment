FROM ubuntu

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update \
    && apt-get -y install \
       git \
       libmysqlclient-dev \
       libpq-dev \
       mysql-server \
       postgresql \
       python-pip \
       python-software-properties \
       software-properties-common \
       wget \
    && add-apt-repository -y ppa:fkrull/deadsnakes \
    && apt-get update \
    && apt-get -y install \
       python2.7-dev \
       python3.2-dev \
       python3.3-dev \
       python3.4-dev \
       python3.5-dev \
       python3.6-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN pip install -U pip
RUN pip install tox

WORKDIR /app/
ADD . /app/

CMD tox