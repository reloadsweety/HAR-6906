 FROM python:3.5-slim

 ENV PYTHONUNBUFFERED 1

 RUN mkdir /app

 WORKDIR /app

 ADD requirements/base.txt /app/

 RUN pip install -r base.txt
 
 ADD . /app/