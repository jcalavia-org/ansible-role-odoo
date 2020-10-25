FROM gitpod/workspace-base

RUN apt-get update && \
    apt-get install -y python && \
    apt-get clean autoclean && \
    apt-get autoremove --yes && \
    rm -rf /var/lib/{apt,dpkg,cache,log}/

RUN pip3 install --upgrade pip && molecule ansible-lint boto3 awscli molecule-ec2