ARG PROXY_REGISTRY_PREFIX
FROM debian:11.6-slim


ARG VERSION="Version Not Set"
ENV VERSION=${VERSION}

# Install dependencies
RUN apt-get update && \
    apt-get install -y \
        apt-transport-https \
        ca-certificates \
        curl \
        gnupg-agent \
        software-properties-common \
        python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Add the Docker GPG key
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -

# Add the stable repository
RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"

# Install Docker
RUN apt-get update && \
    apt-get install -y docker-ce docker-ce-cli containerd.io && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install docker cli
RUN curl -L https://raw.githubusercontent.com/docker/compose-cli/main/scripts/install/install_linux.sh | sh

# Download Docker Compose
#RUN curl -L "https://github.com/docker/compose/releases/download/2.14.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/libexec/docker/cli-plugins/docker-compose

# Make the binary executable
#RUN chmod +x /usr/libexec/docker/cli-plugins/docker-compose


# create API codebase
RUN mkdir /api
COPY /api /api
#COPY /simulators /simulators

# install dependencies
COPY requirements.txt /
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "80"]