#!/usr/bin/env bash

apt-get update

# install pip
apt-get install -y python3-pip
apt-get install -y python3-venv

# update to use the most recent pip
pip3 install --upgrade pip
