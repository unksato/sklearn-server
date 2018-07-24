from python:3
MAINTAINER Satoshi Watanabe <unksato@gmail.com>

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY server /opt/server/
COPY entrypoint.sh /entrypoint.sh
COPY model.joblib /model.joblib

EXPOSE 5000

WORKDIR /opt/server

ENTRYPOINT [ "/entrypoint.sh" ]
