# server
FROM python:latest

ADD ipc_server.py mydata.txt /server/

WORKDIR /server/

VOLUME /server_persistent_storage

EXPOSE 9002

CMD [ "python3", "/server/ipc_server.py" ]
