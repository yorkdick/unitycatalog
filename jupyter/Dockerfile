FROM python:3.12.10

RUN apt-get update && apt-get install -y \
    nodejs npm \
    git \
    curl \
    openjdk-17-jdk \
    build-essential \
    libssl-dev libffi-dev \
    libpq-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && \
    pip install jupyterhub notebook jupyterlab && \
    npm install -g configurable-http-proxy

RUN useradd -m uctest && \
    echo "uctest:uctest" | chpasswd && \
    chown -R uctest:uctest /home/uctest

USER uctest
RUN python -m venv /home/uctest/venv && \
    /home/uctest/venv/bin/pip install --upgrade pip && \
    /home/uctest/venv/bin/pip install pandas pyspark==3.5.5 jupyterlab jupyter_server ipykernel && \
    /home/uctest/venv/bin/python -m ipykernel install --user --name=uctest-venv --display-name "Python(uctest)"

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH="$JAVA_HOME/bin:$PATH"

# 启动 JupyterHub（使用默认配置）
USER root
WORKDIR /srv/jupyterhub
CMD ["jupyterhub"]