FROM ubuntu:latest

RUN apt-get update -y && \
    apt-get install -y python3-pip firefox

RUN pip3 install selenium

COPY my_script.py /app/

CMD ["python3", "/app/my_script.py"]
