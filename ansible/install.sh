#!/bin/bash

yum install -y epel-release yum-priorities python2-pip python-devel telnet

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

#/etc/sysconfig/selinux disabled
#/etc/hosts - 192.168.1.101   server.unixmen.local      server

#/etc/sysconfig/iptables-config
#-A INPUT -m state --state NEW -m tcp -p tcp --dport 80 -j ACCEPT