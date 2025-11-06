# MAC Address to Port Lookup (RESTCONF)

This script connects to a Cisco IOS-XE device via RESTCONF and searches for a specific MAC address in the MAC address table, showing which port it was learned on.

## Requirements

- Python 3.x
- requests library

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

```bash
python mac_to_port.py --host <device_ip> --mac <mac_address> --username <user> --password <pass>
```

### Example

```bash
python mac_to_port.py --host devnetsandboxiosxec9k.cisco.com --mac 0050.56bf.4580 --username admin --password password123
```

### With Custom RESTCONF Port

```bash
python mac_to_port.py --host 192.168.1.1 --mac 0050.56bf.4580 --username admin --password password123 --port 8443
```

## Arguments

| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| `--host` | Yes | - | Device IP address or hostname |
| `--mac` | Yes | - | MAC address to search for (format: xxxx.xxxx.xxxx) |
| `-u`, `--username` | No | cisco | RESTCONF username |
| `-p`, `--password` | No | cisco | RESTCONF password |
| `--port` | No | 443 | RESTCONF port number |

## MAC Address Format

Cisco devices typically use the format: `xxxx.xxxx.xxxx`

Examples:
- `0050.56bf.4580`
- `aabb.cc00.1122`

## Output

The script will display:
- VLAN number
- MAC address
- Type (DYNAMIC or STATIC)
- Interface/Port where the MAC was learned

Example output: