from python:slim-buster

RUN mkdir APP

WORKDIR APP

COPY app.py .

RUN pip3 install flask requests flask_cors 

EXPOSE 80

CMD python ./app.py
