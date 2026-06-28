# System Architecture

## Overview

The DNM-PQC-VPN project combines modern VPN technologies with post-quantum cryptography to provide secure communication between distributed systems.

---

## Components

### VPN Server

- Hosts WireGuard
- Runs Rosenpass
- Controls firewall rules
- Collects monitoring metrics

### Client Nodes

- Connect securely using WireGuard
- Authenticate using Rosenpass
- Access protected services

### Firewall

UFW restricts incoming connections.

### SPA Layer

fwknop provides Single Packet Authorization before VPN access is granted.

### Monitoring

Prometheus collects metrics from the VPN server.

---

## High-Level Architecture

```
Clients
     │
WireGuard Tunnel
     │
Rosenpass Key Exchange
     │
fwknop Authentication
     │
UFW Firewall
     │
VPN Server
     │
Prometheus Monitoring
```