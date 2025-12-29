#!/bin/bash
INSTALL=/opt/proxychains-conf
mkdir $INSTALL
cd $INSTALL
wget https://raw.githubusercontent.com/nathrema/proxychains-conf/refs/heads/main/proxychains-conf.py
ln -s /usr/sbin/proxychains-conf $INSTALL/proxychains-conf.py
chmod +x $INSTALL/proxychains-conf.py
