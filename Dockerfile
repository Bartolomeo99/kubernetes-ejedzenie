FROM python:3.10

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt


RUN pip install -r requirements.txt

COPY . .
EXPOSE 8010

CMD ["python","manage.py","runserver","0.0.0.0:8010"]