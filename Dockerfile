FROM ubuntu:latest



RUN mkdir /setup_web
RUN apt-get update -q && apt-get install -y -q openssh-server
RUN sed -i 's/^PubkeyAuthentication no$/PubkeyAuthentication yes/' /etc/ssh/sshd_config
COPY ./alx.pub /root/.ssh/authorized_keys
COPY ./mysql_key /mysql_key
RUN systemctl enable ssh
COPY ./0-setup_web_static_copy.sh /setup_web
WORKDIR /setup_web
RUN mkdir -p /run/sshd && chmod 755 /run/sshd
RUN apt-get install ufw -y


RUN apt-get install gnupg -y
RUN mkdir -p /etc/apt/trusted.gpg.d
RUN gpg --dearmor -o /etc/apt/trusted.gpg.d/mysql.gpg /mysql_key
RUN sh -c 'echo "deb http://repo.mysql.com/apt/ubuntu bionic mysql-5.7" >> /etc/apt/sources.list.d/mysql.list'
RUN apt-get update
#RUN apt-cache policy mysql-server
RUN echo "mysql-community-server mysql-community-server/root-pass password 123456" | debconf-set-selections
RUN echo "mysql-community-server mysql-community-server/re-root-pass password 123456" | debconf-set-selections

RUN apt install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7* -y

COPY entrypoint.sh /entrypoint.sh
# Give execute permission to the entry point script
RUN chmod +x /entrypoint.sh

RUN apt-get install iputils-ping net-tools -y

#RUN apt-get install -y sudo
#RUN apt-get install iptables sudo -y
#copy firewall.sh /firewall.sh
#RUN sudo -s
#RUN /firewall.sh
ENTRYPOINT ["/entrypoint.sh"]

