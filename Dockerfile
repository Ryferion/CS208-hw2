
FROM python:latest

ADD ipc-server.py /server/

WORKDIR /server/

EXPOSE 9002

CMD [ "python3", "/server/ipc-server.py" ]
