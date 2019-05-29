FROM python:3.6

RUN mkdir /upload_app
WORKDIR /upload_app
ADD ./requirements.txt /upload_app
RUN pip install -r requirements.txt
ADD . ./upload_app/
