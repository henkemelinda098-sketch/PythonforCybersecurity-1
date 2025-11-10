#!/usr/bin/env python3
# Script that scans web server logs for possible hacking
# Use RegEx to find and report on common hacking types
# Based on https://www.cgisecurity.com/fingerprinting-port80-attacks-a-look-into-web-server-and-web-application-attack-signatures-part-two.html
# By Melinda Henke 11/9

import re
from collections import Counter

# Define the path to your log file
log_file_path = 'access.log'

# Regular expression to extract the resource path from each log line
resource_pattern = re.compile(r'\"(?:GET|POST) (\S+)')

# Counter to track resource access frequency
resource_counter = Counter()

# Read and process the log file
with open(log_file_path, 'r') as file:
    for line in file:
        match = resource_pattern.search(line)
        if match:
            resource = match.group(1)
            resource_counter[resource] += 1

# Generate and display the report
print("Most Accessed Resources:")
for resource, count in resource_counter.most_common():
    print(f"{resource}: {count} accesses")
