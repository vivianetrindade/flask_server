FROM ubuntu:latest

# Install SQLite
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y sqlite3 libsqlite3-dev python3 python3-pip
RUN /usr/bin/sqlite3 --version


RUN mkdir /src
ADD . /src
WORKDIR /src
RUN pip install -r requirements.txt

ENV SQL_DB_PATH=/src/db/dibz.db
RUN /src/db/init_db.sh

#RUN FLASK_APP=main.py FLASK_ENV=development flask run --host=0.0.0.0

CMD /bin/bash start.sh

VOLUME /src