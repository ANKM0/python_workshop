FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    curl build-essential git && \
    apt-get clean

RUN useradd -m vscode
USER vscode
WORKDIR /home/vscode

RUN curl -sSL https://install.python-poetry.org | python3 - && \
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc

ENV PATH="/home/vscode/.local/bin:$PATH"
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /workspace

COPY pyproject.toml poetry.lock* ./
RUN poetry install --no-root --no-interaction --no-ansi

COPY . .
