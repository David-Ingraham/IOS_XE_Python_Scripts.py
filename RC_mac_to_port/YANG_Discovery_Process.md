# YANG Model Discovery Process

## Step 1: Check IOS-XE Version

First, I opened a shell on the device and checked the version:

```bash
ssh username@devnetsandboxiosxec9k.cisco.com
```

```
CAT9k_AO#show version
Cisco IOS XE Software, Version 17.15.01
Cisco IOS Software [IOSXE], Catalyst L3 Switch Software (CAT9K_IOSXE)
Version 17.15.1, RELEASE SOFTWARE (fc4)
```

**Version:**  IOS-XE 17.15.1

## Step 2: Find YANG Model Documentation

Searched for documentation and found the YANG model repository:
- **Repository:** https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151
- This repo contains all available YANG models for IOS-XE 17.15.1

## Step 3: Query the RESTCONF Endpoint

Queried the MATM (MAC Address Table Manager) endpoint to get the JSON structure:

```bash
curl -k -u admin:password123 \
  -H "Accept: application/yang-data+json" \
  https://devnetsandboxiosxec9k.cisco.com:443/restconf/data/Cisco-IOS-XE-matm-oper:matm-oper-data \
  > matm-oper-data.json
```

**Endpoint Used:** `/restconf/data/Cisco-IOS-XE-matm-oper:matm-oper-data`

## Step 4: Parse JSON Structure

Learned the key-pair structure from the JSON response and coded Python to walk through the data:

- Root: `Cisco-IOS-XE-matm-oper:matm-oper-data`
- Tables: `matm-table[]`
- Entries: `matm-mac-entry[]`
- Fields: `mac`, `port`, `vlan-id-number`, `mat-addr-type`











