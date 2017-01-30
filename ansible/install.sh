#!/bin/bash

yum install -y epel-release python2-pip python-devel

pip install ansible pexpect

setsebool -P httpd_can_network_connect 1

