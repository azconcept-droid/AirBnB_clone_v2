#!/usr/bin/env bash
# This script that sets up your web servers for the deployment of web_static

TESTDIREXIT='/data/web_static/releases/test/'
CURRENTDIREXIT='/data/web_static/current/'

apt install -y nginx

if [ -d $TESTDIREXIT ] then;
	rm -rf /data/web_static/current/
fi
if [ -d $CURRENTDIREXIT ] then;
	rm -rf /data/web_static/releases/test/
fi
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/current
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test
touch /data/web_static/releases/test/index.html
echo "Hello world" >> data/web_static/releases/test/index.html
ln -s /data/web_static/current/ /data/web_static/releases/test/
chown ubuntu:ubuntu -R /data/
mkdir /var/www/hbnb_static
ln -s /data/web_static/current /etc/nginx/site-enabled

