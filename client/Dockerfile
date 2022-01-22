# client
FROM python:latest

ADD ipc_client.py /client/

WORKDIR /client/

VOLUME /client_persistent_storage

CMD [ "python3", "/client/ipc_client.py" ]
