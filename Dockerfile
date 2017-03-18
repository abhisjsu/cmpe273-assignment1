FROM python:2.7.13
MAINTAINER Abhishek Chaudhary "abhishek.chaudhary@sjsu.edu"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python",app.py]
CMD [$1]
