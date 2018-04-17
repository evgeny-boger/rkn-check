#!/usr/bin/python3

import os, sys, csv
import netaddr
ips = []
for line in sys.stdin:
    line = line.strip()
    if line:
        ips.append(line)

subnets = []
with open(sys.argv[1],errors='ignore') as csv_file:
    csv_file.readline()
    for row in csv.reader(csv_file, delimiter=';'):
        if row:
            row_subnets_str = row[0]
            subnets_parts = row_subnets_str.split('|')
            for s in subnets_parts:
                s = s.strip()
                if s:
                    if '/' in s:
                        subnets.append(s)


for ip in ips:
    print(ip, netaddr.all_matching_cidrs(ip, subnets ))



