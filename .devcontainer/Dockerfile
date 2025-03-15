FROM mcr.microsoft.com/devcontainers/python:3.12

USER vscode

RUN curl -sSf https://rye.astral.sh/get | RYE_VERSION="0.44.0" RYE_INSTALL_OPTION="--yes" bash
ENV PATH=/home/vscode/.rye/shims:$PATH

RUN echo "[[ -d .venv ]] && source .venv/bin/activate || export PATH=\$PATH" >> /home/vscode/.bashrc
