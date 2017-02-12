#!/bin/bash

yum install -y epel-release yum-priorities python2-pip python-devel

pip install --upgrade pip
pip install --upgrade setuptools
pip install ansible pexpect

setsebool -P httpd_can_network_connect 1

#vim /etc/yum.repos.d/CentOS-Base.repo
#  Add the following to sections base and update
#    exclude=postfix-*
#    priority=1 
#  Modify the following in section centosplus
#    priority=2
#    enabled=1

#yum erase postfix
#yum install postfix
#postconf -c /etc/postfix -m | grep sql
#  mysql
#  pgsql