FROM python:3.11.5
ENV PYTHONUNBUFFERED 1
WORKDIR /order
COPY requirements.txt /order/requirements.txt
RUN pip install -r requirements.txt
COPY . /order

CMD python3 manage.py runserver 0.0.0.0:8000