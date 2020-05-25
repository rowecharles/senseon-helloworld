FROM python:3.8.3-alpine

COPY webserver.py /srv/webserver.py

ENTRYPOINT [ "python", "/srv/webserver.py" ]
