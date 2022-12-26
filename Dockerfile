
FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /app/

# running migrations
#RUN python3 manage.py migrate
#CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]