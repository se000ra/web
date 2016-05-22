#! /bin/sh
#
# init.sh
# Copyright (C) 2016 van <van@vanleno>
#
# Distributed under terms of the MIT license.
#
#nginx conf
sudo rm /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart


#gunicorn conf
sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart
