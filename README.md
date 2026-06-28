# DNM-PQC-VPN

## Project Overview

DNM-PQC-VPN is a secure VPN solution that combines WireGuard with Rosenpass to provide post-quantum cryptography (PQC) protection. The project is designed to demonstrate a modern VPN architecture that is resilient against both current and future cryptographic threats.

---

## Problem Statement

Traditional VPN protocols rely on classical cryptographic algorithms that may become vulnerable with the advancement of quantum computing.

This project addresses that issue by integrating:

- WireGuard for high-performance VPN tunneling
- Rosenpass for post-quantum key exchange
- fwknop for Single Packet Authorization (SPA)
- UFW for firewall management
- Prometheus for monitoring and metrics collection

---

## Architecture Overview

The system consists of:

- VPN Server
- Bank Client Virtual Machines
- WireGuard Tunnel
- Rosenpass Key Exchange
- fwknop Authentication Layer
- UFW Firewall
- Prometheus Monitoring

Detailed architecture documentation is available in:

- docs/architecture.md

---

## Quick Start (10 Minutes)

### 1. Clone the repository

```bash
git clone https://github.com/janevgln/DNM-PQC-VPN.git
```

### 2. Enter the project directory

```bash
cd DNM-PQC-VPN
```

### 3. Install dependencies

```bash
bash scripts/install_dependencies.sh
```

### 4. Configure the VPN

Edit:

- network/wg0.conf
- network/rosenpass.toml

### 5. Start the VPN service

```bash
sudo wg-quick up wg0
```

---

## Running Tests

Execute:

```bash
bash testing/pentest.sh
```

or

```bash
bash testing/load_test.sh
```

or

```bash
bash testing/edge_case_tests.sh
```

---

## Documentation

Detailed documentation is available below:

| Document | Description |
|----------|-------------|
| [Architecture](docs/architecture.md) | System architecture and components |
| [Setup Guide](docs/setup_guide.md) | Installation and deployment guide |
| [Testing Guide](docs/testing_guide.md) | Security and performance testing |

---

## License

This project is distributed under the MIT License.

---

## AI Usage

See AI_USAGE.md for details regarding AI-assisted development.