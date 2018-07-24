from python:2
MAINTAINER Satoshi Watanabe <unksato@gmail.com>

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY server /opt/server/
COPY entrypoint.sh /entrypoint.sh

EXPOSE 5000

WORKDIR /opt/server

ENTRYPOINT [ "/entrypoint.sh" ]
