#!/usr/bin/env python
#
# This script connects to a Cisco device via RESTCONF and searches for a MAC address
# in the MAC address table, returning the port where it was learned.

import sys
import requests
from argparse import ArgumentParser
from requests.auth import HTTPBasicAuth
import urllib3

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

if __name__ == '__main__':
    parser = ArgumentParser(description='Lookup MAC address to port mapping via RESTCONF')
    # Input parameters
    parser.add_argument('--host', type=str, required=True,
                        help="The device IP or DN")
    parser.add_argument('-u', '--username', type=str, default='cisco',
                        help="Username")
    parser.add_argument('-p', '--password', type=str, default='cisco',
                        help="Password")
    parser.add_argument('--port', type=int, default=443,
                        help="RESTCONF port (default: 443)")
    parser.add_argument('--mac', type=str, required=True,
                        help="MAC address to search for")
    parser.add_argument('-v', '--verbose', action='store_true',
                        help="Show full MAC table entry details")
    args = parser.parse_args()

    # RESTCONF URL for MAC address table (MATM - MAC Address Table Manager)
    url = f"https://{args.host}:{args.port}/restconf/data/Cisco-IOS-XE-matm-oper:matm-oper-data"
    
    headers = {
        'Accept': 'application/yang-data+json',
        'Content-Type': 'application/yang-data+json'
    }

    try:
        response = requests.get(
            url,
            auth=HTTPBasicAuth(args.username, args.password),
            headers=headers,
            verify=False,
            timeout=10
        )
        response.raise_for_status()
        
        data = response.json()
        found = False
        search_mac = args.mac.lower().replace('.', '').replace(':', '').replace('-', '')
        
        # Parse MATM operational data for MAC addresses
        if 'Cisco-IOS-XE-matm-oper:matm-oper-data' in data:
            matm_data = data['Cisco-IOS-XE-matm-oper:matm-oper-data']
            if 'matm-table' in matm_data:
                for table in matm_data['matm-table']:
                    if 'matm-mac-entry' in table:
                        for mac_entry in table['matm-mac-entry']:
                            mac_addr = mac_entry.get('mac', '').lower().replace('.', '').replace(':', '').replace('-', '')
                            if search_mac in mac_addr:
                                found = True
                                if args.verbose:
                                    # Show full entry details
                                    vlan = mac_entry.get('vlan-id-number', 'N/A')
                                    mac = mac_entry.get('mac', 'N/A')
                                    port = mac_entry.get('port', 'N/A')
                                    addr_type = mac_entry.get('mat-addr-type', 'N/A')
                                    table_type = mac_entry.get('table-type', 'N/A')
                                    print(f"MAC: {mac}, Port: {port}, VLAN: {vlan}, Type: {addr_type}, Table: {table_type}")
                                else:
                                    # Just show the port
                                    print(mac_entry.get('port', 'N/A'))
        
        if not found:
            print(f"No entry found for MAC address: {args.mac}")
            
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)