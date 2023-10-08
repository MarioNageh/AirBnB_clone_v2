#!/usr/bin/env bash
# INstall Nginx if not already installed
apt-get update
apt-get -y install nginx
apt-get -y install net-tools


# Create the folder /data/ if it doesn’t already exist
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Create a fake HTML file /data/web_static/releases/test/index.html
echo "Mario -_-" | tee /data/web_static/releases/test/index.html

# Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sh -c 'echo "
server {
    listen 80;
    listen [::]:80 default_server;
    server_name localhost;

    location /hbnb_static {
        alias /data/web_static/current/;
        index index.html;
    }
}

" > /etc/nginx/sites-available/default'
update-rc.d nginx enable
service nginx restart
