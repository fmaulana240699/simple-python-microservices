from python:slim-buster

RUN mkdir APP

WORKDIR APP

COPY buku.py .

RUN pip3 install flask requests flask_cors socket

EXPOSE 5555

CMD python ./buku.py
