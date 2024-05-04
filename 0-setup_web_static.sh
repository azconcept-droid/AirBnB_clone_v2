#!/usr/bin/env bash
# This script that sets up your web servers for the deployment of web_static

# Define the symbolic link path
link_path="/data/web_static/current"

# Install nginx if not already installed
if dpkg-query -l nginx >/dev/null 2>&1; then
	:
else
	apt install -y nginx
fi
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test
touch /data/web_static/releases/test/index.html
cat > /data/web_static/releases/test/index.html <<EOF
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF
# Check if the symbolic link exists
if [ -L "$link_path" ]; then
	rm "$link_path"
	ln -s /data/web_static/releases/test "$link_path"
else
	ln -s /data/web_static/releases/test "$link_path"
fi

chown ubuntu:ubuntu -R /data/
# sed -i 's+/var/www/html+/data/web_static/current+g' /etc/nginx/sites-available/default
sed -i 's+_;+_;\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}+g' /etc/nginx/sites-available/default
service nginx restart
