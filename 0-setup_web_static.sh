#!/usr/bin/env bash
# Script to install web static server

# Update system
sudo apt-get update
sudo apt-get -y install nginx

# Create directories if they don't already exist
sudo mkdir -p /data/web_static/releases/test
sudo mkdir /data/web_static/shared/

# Create fake file
printf %s "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

# Create sym link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to ubuntu user and groups
chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve the content of /data/web_static/current/
# to hbnb_static (ex: https://papirico.tech/hbnb_static)
config_file=/etc/nginx/sites-available/default
sed -i '29a \ \tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' $config_file
sudo service nginx restart
