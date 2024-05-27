# ./django-nija/Dockerfile

# Etapa de build
FROM python:3.11-slim AS builder

ENV TZ=America/Sao_Paulo
ENV NODE_VERSION=20.11.1

# Instalar dependências necessárias
RUN apt-get update && \
    apt-get install -y curl build-essential libmariadb3 libmariadb-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Instalar Node.js usando nvm
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash && \
    export NVM_DIR="$HOME/.nvm" && \
    [ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh" && \
    nvm install ${NODE_VERSION} && \
    nvm use ${NODE_VERSION} && \
    nvm alias default ${NODE_VERSION}

WORKDIR /app

# Criar e ativar ambiente virtual
RUN python3 -m venv /venv

# Definir PATH do ambiente virtual
ENV PATH="/venv/bin:$PATH"

# Copiar arquivo requirements.txt e instalar dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt --upgrade

# Etapa final
FROM python:3.11-slim

# Instalar dependências necessárias para execução
RUN apt-get update && \
    apt-get install -y libmariadb3 libmariadb-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copiar dependências instaladas e código da aplicação
COPY --from=builder /venv /venv
COPY ./src .

# Definir PATH do ambiente virtual
ENV PATH="/venv/bin:$PATH"

EXPOSE 8000

CMD ["bash", "-c", "source /venv/bin/activate && python manage.py runserver 0.0.0.0:8000"]


