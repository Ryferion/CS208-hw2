
FROM python:latest

ADD ipc-server.py 

WORKDIR /

EXPOSE 9002

CMD [ "python3", "/ipc-server.py" ]
