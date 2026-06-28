#!/bin/bash

echo "Applying UFW Rules..."

sudo ufw default deny incoming
sudo ufw default allow outgoing

sudo ufw allow 22/tcp
sudo ufw allow 51820/udp

sudo ufw enable

echo "Firewall configuration completed."