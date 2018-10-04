FROM ubuntu:16.04

ADD ai-gan /

RUN apt-get update && apt-get install -y

RUN apt-get install -y python3-dev python3-pip libgtk2.0-dev

RUN pip3 install -r requirements.txt

CMD ["python3" , "in.py"]

