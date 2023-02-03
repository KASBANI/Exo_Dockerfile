FROM ubuntu

WORKDIR /

RUN apt update && apt install python3 -y

COPY pgcd.py .

CMD python3 pgcd.py