#!/bin/bash

yum install -y epel-release python2-pip python-devel

pip install --upgrade pip
pip install --upgrade setuptools
pip install ansible pexpect

setsebool -P httpd_can_network_connect 1

