FROM python:3.7.4-buster

RUN pip install praw==6.3.1
RUN pip install mysql-connector-python==8.0.17
RUN pip install schedule==0.6.0
RUN pip --no-cache-dir install pandas==0.24.2

COPY redditquery /usr/bin/redditquery
RUN chmod +x /usr/bin/redditquery/run.sh
WORKDIR /usr/bin/redditquery
ENTRYPOINT ./run.sh


