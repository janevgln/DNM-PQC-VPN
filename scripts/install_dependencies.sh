#!/bin/bash

echo "Installing dependencies..."

sudo apt update

sudo apt install -y \
wireguard \
ufw \
fwknop-server \
python3 \
python3-pip

echo "Dependencies installed."