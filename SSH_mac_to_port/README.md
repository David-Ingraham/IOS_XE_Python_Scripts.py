# MAC Address to Port Lookup

This script connects to a Cisco IOS/IOS-XE device via SSH and searches for a specific MAC address in the MAC address table, showing which port it was learned on.

## Requirements

- Python 3.x
- netmiko library

## Installation

```bash
pip install netmiko
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

### With Custom SSH Port

```bash
python mac_to_port.py --host 192.168.1.1 --mac 0050.56bf.4580 --username admin --password password123 --port 2222
```

## Arguments

| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| `--host` | Yes | - | Device IP address or hostname |
| `--mac` | Yes | - | MAC address to search for (format: xxxx.xxxx.xxxx) |
| `-u`, `--username` | No | cisco | SSH username |
| `-p`, `--password` | No | cisco | SSH password |
| `--port` | No | 22 | SSH port number |

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
```
  1    0050.56bf.7731    STATIC      Vl1 
```

## Notes

- This script uses SSH (port 22 by default)
- The device must have SSH enabled
- You need proper credentials with privilege to run show commands
- If no MAC address is found, the script will indicate no entry was found

