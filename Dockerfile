FROM python:3.6

MAINTAINER Ashley Collinge "me@ashleycollinge.co.uk"

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

COPY . /app

RUN pip3.6 install -r requirements.txt

ENTRYPOINT [ "python3.6" ]

CMD [ "run.py" ]
