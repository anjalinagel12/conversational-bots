# UseCase: Rasa 1.10.16 Setup

FROM ubuntu:18.04

RUN echo "Starting to Build Image for Rasa 1.10.16"
RUN echo "ubuntu 18.04 Version"

RUN apt-get update \
    && apt-get install -y \
    python3 \
    python3-pip \
    curl \
    g++ \
    vim \
    git \
    && ln -s /usr/bin/python3 /usr/bin/python \
    && ln -s /usr/bin/pip3 /usr/bin/pip \
    && export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/local/lib:/usr/bin/python \
    && /usr/bin/pip install --upgrade pip \
    && pip3 install rasa==1.10.16 \
    && export LANG=C.UTF-8
