#!/bin/bash

# Run MsSQL Server
service mysql start

/usr/sbin/sshd -D && tail -f /dev/null
