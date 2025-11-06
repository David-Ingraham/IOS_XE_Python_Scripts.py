#!/usr/bin/env python
"""
Fetch running configuration from Cisco IOS-XE device via RESTCONF
and save to a JSON file.
"""
import requests
import urllib3
import json
import sys
import os
from datetime import datetime

if __name__ == '__main__':
    # Disable SSL Warnings
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    # Get config from environment variables
    host = os.getenv('SWITCH_HOST')
    username = os.getenv('SWITCH_USERNAME')
    password = os.getenv('SWITCH_PASSWORD')
    port = os.getenv('SWITCH_PORT', '443')
    output_file = os.getenv('OUTPUT_FILE', 'active_config.json')
    
    # Validate required vars
    if not host or not username or not password:
        print("Error: Required environment variables missing:", file=sys.stderr)
        print("  SWITCH_HOST, SWITCH_USERNAME, SWITCH_PASSWORD", file=sys.stderr)
        sys.exit(1)
    
    url = f"https://{host}:{port}/restconf/data/Cisco-IOS-XE-native:native"
    
    headers = {
       "Content-Type": "application/yang-data+json",
       "Accept": "application/yang-data+json",
    }
    
    try:
        print(f"Fetching config from {host}...")
        response = requests.get(
            url, 
            headers=headers, 
            auth=(username, password), 
            verify=False,
            timeout=30
        )
        response.raise_for_status()
        
        config_data = response.json()
        
        # Add metadata
        metadata = {
            "snapshot_time": datetime.utcnow().isoformat() + "Z",
            "device": host,
            "config": config_data
        }
        
        # Save to file
        with open(output_file, 'w') as f:
            json.dump(metadata, f, indent=2)
        
        print(f" Config saved to {output_file}")
        print(f" Snapshot time: {metadata['snapshot_time']}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)