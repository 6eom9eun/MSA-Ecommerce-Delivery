FROM python:3.11.5
ENV PYTHONUNBUFFERED 1
RUN mkdir /boss
WORKDIR /boss
ADD requirements.txt /boss/
RUN pip install -r requirements.txt
ADD . /boss/