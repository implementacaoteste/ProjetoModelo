# ./Dockerfile

FROM ubuntu:22.04

ENV TZ=America/Sao_Paulo
ENV NODE_VERSION=20.11.1

# Instalar curl e nvm, depois Node.js
RUN apt-get update && \
    apt-get install -y curl && \
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash && \
    export NVM_DIR="$HOME/.nvm" && \
    [ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh" && \
    [ -s "$NVM_DIR/bash_completion" ] && . "$NVM_DIR/bash_completion" && \
    nvm install ${NODE_VERSION}

WORKDIR /app

# Instalar Python, pacotes de desenvolvimento, e libmysqlclient-dev
RUN apt-get update -y && apt-get install -y \
    python3.11 python3.11-venv python3-pip \
    python3.11-dev build-essential libmysqlclient-dev # tzdata

# Configurar fuso horário
# RUN ln -fs /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime
# RUN dpkg-reconfigure --frontend noninteractive tzdata

# Criar e ativar ambiente virtual
RUN python3.11 -m venv /venv

# Definir PATH do ambiente virtual
ENV PATH="/venv/bin:$PATH"

# Copiar arquivo requirements.txt e instalar dependências
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt --upgrade

EXPOSE 8000

CMD ["bash", "-c", "source /venv/bin/activate && python3.11 manage.py runserver 0.0.0.0:8000"]
