# Setup Guide

## Requirements

- Ubuntu 24.04 LTS
- WireGuard
- Rosenpass
- fwknop
- UFW
- Python 3
- Prometheus

---

## Installation

### Clone Repository

```bash
git clone https://github.com/janevgln/DNM-PQC-VPN.git
```

### Enter Project

```bash
cd DNM-PQC-VPN
```

### Install Dependencies

```bash
bash scripts/install_dependencies.sh
```

### Configure WireGuard

Edit:

- network/wg0.conf

### Configure Rosenpass

Edit:

- network/rosenpass.toml

### Configure Firewall

```bash
bash network/ufw/firewall_rules.sh
```

### Start VPN

```bash
sudo wg-quick up wg0
```