FROM --platform=linux/amd64 python:3.8

ENV PYTHONPATH "${PYTHONPATH}:/"

COPY requirements.txt ./
RUN pip install -r requirements.txt

WORKDIR database
COPY database ./

WORKDIR ../tests
COPY tests ./

WORKDIR ../src
COPY src ./

CMD python app.py