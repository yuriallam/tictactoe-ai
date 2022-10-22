FROM python:3.10.7-alpine

WORKDIR /server

COPY ./requirements.txt ./
RUN pip3 install -r requirements.txt

COPY ./src .

CMD python3 main.py