FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y netcat

WORKDIR /code

ADD main.py /code
ADD connectionmethods.py /code
ADD dbmethods.py /code
COPY requirements.txt /code
COPY entrypoint.sh /code



RUN python -m pip install -r requirements.txt

# Wait for message queue to be up
ENTRYPOINT ["bash", "entrypoint.sh"]

CMD ["python", "main.py"]