from python:slim-buster

RUN mkdir APP

WORKDIR APP

COPY buku.py .

RUN pip3 install flask requests flask_cors aws_xray_sdk

EXPOSE 5001

CMD python ./buku.py
