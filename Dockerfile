FROM python:3.7-alpine
MAINTAINER V7hinc

WORKDIR /tmp

# 安装必要插件
RUN set -x;\
apk add --no-cache libffi libheif-dev libde265-dev git;

# 安装pyheif
RUN set -x;\
pip install git+https://github.com/carsales/pyheif.git;\
mkdir /python

COPY . /python/



