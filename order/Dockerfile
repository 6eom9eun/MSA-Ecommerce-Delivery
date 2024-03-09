FROM python:3.11.5
ENV PYTHONUNBUFFERED 1
RUN mkdir /order
WORKDIR /order
ADD requirements.txt /order/
RUN pip install -r requirements.txt
ADD . /order/