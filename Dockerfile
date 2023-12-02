FROM python:3.10

WORKDIR /ads

RUN pip install --upgrade pip

COPY requirements.txt /ads

RUN pip install -r requirements.txt

COPY . .