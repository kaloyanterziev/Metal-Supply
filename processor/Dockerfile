FROM ubuntu:bionic

RUN \
 apt-get update \
 && apt-get install -y -q curl gnupg \
 && curl -sSL 'http://keyserver.ubuntu.com/pks/lookup?op=get&search=0x8AA7AF1F1091A5FD' | apt-key add -  \
 && echo 'deb [arch=amd64] http://repo.sawtooth.me/ubuntu/chime/stable bionic universe' >> /etc/apt/sources.list \
 && apt-get update

RUN apt-get install -y apt-transport-https

RUN apt-get install -y -q python3-sawtooth-sdk

WORKDIR /project/metal-supply

ENV PATH $PATH:/project/metal-supply/bin

CMD ['metal-supply-tp']