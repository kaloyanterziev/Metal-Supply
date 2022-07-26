# Copyright 2018 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------------------
# Modifications copyright (C) 2022 <Kaloyan Terziev>

FROM ubuntu:bionic

RUN \
 apt-get update \
 && apt-get install -y -q curl gnupg \
 && curl -sSL 'http://keyserver.ubuntu.com/pks/lookup?op=get&search=0x8AA7AF1F1091A5FD' | apt-key add -  \
 && echo 'deb [arch=amd64] http://repo.sawtooth.me/ubuntu/chime/stable bionic universe' >> /etc/apt/sources.list \
 && apt-get update

RUN apt-get install -y apt-transport-https

RUN apt-get install -y --allow-unauthenticated -q \
    curl \
    python3-pip \
    python3-dev \
    libpq-dev \
    python3-sawtooth-cli \
    python3-sawtooth-sdk \
    python3-sawtooth-rest-api

RUN curl -sL https://deb.nodesource.com/setup_14.x -o nodesource_setup.sh \
    && bash nodesource_setup.sh \
    && apt-get install -y nodejs \
    && npm --version \
    && node --version

RUN pip3 install \
    aiohttp \
    aiopg \
    bcrypt \
    grpcio-tools==1.29.0 \
    itsdangerous \
    nose2 \
    psycopg2-binary \
    pycrypto \
    pylint \
    pycodestyle

WORKDIR /project/metal-supply

#COPY metal_supply_app/package.json /project/metal-supply/metal_supply_app/
#
#RUN cd metal_supply_app/ && npm install

ENV PATH $PATH:/project/metal-supply/bin
