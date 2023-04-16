FROM ubuntu:latest

RUN apt-get update -y

RUN apt-get install python3 -y

RUN apt-get update && apt-get install -y gnupg

RUN apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 0xcbcb082a1bb943db
RUN curl -LsS https://downloads.mariadb.com/MariaDB/mariadb_repo_setup | bash
RUN apt install gcc libmariadb3 libmariadb-dev mariadb-client sqlite3 libsqlite3-dev openssl python3-pip -y

RUN pip3 install --upgrade pip
RUN pip3 install packaging

RUN apt-get update -y
RUN apt-get upgrade -y

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app
RUN pip3 install -r requirements.txt
COPY . /app

EXPOSE 3306/tcp
EXPOSE 5000/tcp
ENTRYPOINT [ "python" ]
CMD [ "run.py" ]

