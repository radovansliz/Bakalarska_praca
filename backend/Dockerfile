ARG PROXY_REGISTRY_PREFIX
FROM ${PROXY_REGISTRY_PREFIX:-docker.io}/python:3.9.6-slim-buster

ARG VERSION="Version Not Set"
ENV VERSION=${VERSION}

# install compiler and clean
RUN apt-get update && \
    apt-get install gcc -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# create API codebase
RUN mkdir /api
COPY /api /api

RUN echo "ficime"

# install dependencies
COPY requirements.txt /
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "80"]