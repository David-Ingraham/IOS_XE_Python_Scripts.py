#!/usr/bin/env python
#
# This script connects to a Cisco device via SSH and searches for a MAC address
# in the MAC address table, returning the port where it was learned.

import sys
from argparse import ArgumentParser
from netmiko import ConnectHandler

if __name__ == '__main__':
    parser = ArgumentParser(description='Lookup MAC address to port mapping')
    # Input parameters
    parser.add_argument('--host', type=str, required=True,
                        help="The device IP or DN")
    parser.add_argument('-u', '--username', type=str, default='cisco',
                        help="Username")
    parser.add_argument('-p', '--password', type=str, default='cisco',
                        help="Password")
    parser.add_argument('--port', type=int, default=22,
                        help="SSH port")
    parser.add_argument('--mac', type=str, required=True,
                        help="MAC address to search for")
    args = parser.parse_args()

    device = {
        'device_type': 'cisco_ios',
        'host': args.host,
        'username': args.username,
        'password': args.password,
        'port': args.port,
    }

    try:
        with ConnectHandler(**device) as conn:
            command = f"show mac address-table | include {args.mac}"
            output = conn.send_command(command)
            
            if output.strip():
                print(output)
            else:
                print(f"No entry found for MAC address: {args.mac}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
