
FROM python:latest

ADD ipc_server.py /server/

WORKDIR /server/

EXPOSE 9002

CMD [ "python3", "/server/ipc_server.py" ]
