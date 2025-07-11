FROM jupyterhub/jupyterhub:latest

USER root

RUN apt-get update && \
    apt-get install -y --no-install-recommends openjdk-17-jdk && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir pyspark==3.5.5 jupyterlab jupyter_server && \
    useradd -m uctest && \
    echo "uctest:uctest" | chpasswd

CMD ["jupyterhub"]
