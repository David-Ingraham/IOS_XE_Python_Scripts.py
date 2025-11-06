# IOS XE Python Scripts

Inspired by the [CiscoDevNet/python_code_samples_network](https://github.com/CiscoDevNet/python_code_samples_network) repository.

## Project Structure

```
.
├── .github/workflows/          # Automated config snapshots (runs every 4 hours)
├── active_config.json          # Latest device config (auto-updated by workflow)
├── SSH_mac_to_port/            # MAC-to-port lookup via SSH
├── RC_mac_to_port/             # MAC-to-port lookup via RESTCONF
└── RC_get_config/              # Get running config via RESTCONF
```

## Scripts

- **SSH_mac_to_port** - Look up MAC address to port mapping via SSH
- **RC_mac_to_port** - Look up MAC address to port mapping via RESTCONF API
- **RC_get_config** - Fetch running configuration via RESTCONF API

## Automated Config Snapshots

`active_config.json` contains the latest device configuration, automatically fetched every 4 hours via GitHub Actions. Git history tracks all configuration changes over time.

## Testing Environment

Scripts are tested against the Catalyst 9000 Always-On Sandbox from Cisco DevNet.

## Requirements

Each script directory contains its own requirements.txt file.

