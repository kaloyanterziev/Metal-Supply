FROM ubuntu:bionic

RUN \
 apt-get update \
 && apt-get install -y -q curl gnupg \
 && curl -sSL 'http://keyserver.ubuntu.com/pks/lookup?op=get&search=0x8AA7AF1F1091A5FD' | apt-key add -  \
 && echo 'deb [arch=amd64] http://repo.sawtooth.me/ubuntu/chime/stable bionic universe' >> /etc/apt/sources.list \
 && apt-get update

RUN apt-get install -y apt-transport-https

RUN apt-get install -y --allow-unauthenticated -q python3-grpcio-tools \
    python3-pip \
    python3-dev \
    libpq-dev \
    python3-sawtooth-rest-api \
    python3-sawtooth-sdk

RUN pip3 install \
    async-timeout==3.0.1 \
    aiohttp \
    aiopg \
    bcrypt \
    itsdangerous \
    pycrypto \
    psycopg2-binary


WORKDIR /project/metal-supply

ENV PATH $PATH:/project/metal-supply/bin

EXPOSE 8000/tcp

CMD ['metal-supply-rest-api']
