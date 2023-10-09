FROM ubuntu:latest



RUN mkdir /setup_web
RUN apt-get update -q && apt-get install -y -q openssh-server
RUN sed -i 's/^PubkeyAuthentication no$/PubkeyAuthentication yes/' /etc/ssh/sshd_config
COPY ./alx.pub /root/.ssh/authorized_keys
RUN systemctl enable ssh
COPY ./0-setup_web_static_copy.sh /setup_web
WORKDIR /setup_web
RUN mkdir -p /run/sshd && chmod 755 /run/sshd

COPY entrypoint.sh /entrypoint.sh
# Give execute permission to the entry point script
RUN chmod +x /entrypoint.sh
# Set the entry point script
ENTRYPOINT ["/entrypoint.sh"]

