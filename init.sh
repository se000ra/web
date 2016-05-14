#! /bin/sh
#
# init.sh
# Copyright (C) 2016 van <van@vanleno>
#
# Distributed under terms of the MIT license.
#


sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx.conf
sudo /etc/init.d/nginx restart
