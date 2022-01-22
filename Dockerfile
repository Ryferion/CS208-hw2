# server
# FROM python:latest

# ADD ipc_server.py mydata.txt /server/

# WORKDIR /server/

# EXPOSE 9002

# CMD [ "python3", "/server/ipc_server.py" ]


# client
FROM python:latest

ADD ipc_client.py /client/

WORKDIR /client/

CMD [ "python3", "/client/ipc_client.py" ]
