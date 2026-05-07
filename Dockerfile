FROM python:3.10-slim

WORKDIR /morshch

COPY env_1.py .
COPY 6-morshch.py .


CMD ["tail", "-f", "/dev/null"]
