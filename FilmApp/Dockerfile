from python:slim-buster

RUN mkdir APP

WORKDIR APP

COPY film.py .

RUN pip3 install flask requests flask_cors 

EXPOSE 5000

CMD python ./film.py
