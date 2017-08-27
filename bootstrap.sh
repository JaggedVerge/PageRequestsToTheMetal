#!/usr/bin/env bash

apt-get update

# install pip
apt-get install -y python-pip

# update to use the most recent pip
pip install --upgrade pip
