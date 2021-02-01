FROM python:3.7.2-alpine3.9


# RUN mkdir /flask
WORKDIR /colors-api

# Install lib 
COPY ./requirements.txt ./

RUN pip install -r requirements.txt

EXPOSE 5000
CMD [ "python" "run.py" ]