#!/usr/bin/env bash
# INstall Nginx if not already installed
sudo apt-get update
sudo apt-get -y install nginx

# Create the folder /data/ if it doesn’t already exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file /data/web_static/releases/test/index.html
echo "Mario -_-" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sudo sh -c 'echo "
server {
    listen 80;
    listen [::]:80 default_server;
    server_name localhost;

    location /hbnb_static {
        alias /data/web_static/current/;
        index index.html index.htm;
    }
}

" > /etc/nginx/sites-available/default'
sudo service nginx restart
