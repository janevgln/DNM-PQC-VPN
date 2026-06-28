#!/bin/bash

echo "Cleaning project..."

sudo wg-quick down wg0

sudo ufw disable

echo "Cleanup finished."