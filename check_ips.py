#!/usr/bin/python3

import os, sys, csv
import netaddr


def check_ips(ips):
    status = False
    for ip in ips:
        matching = netaddr.all_matching_cidrs(ip, subnets )
        if matching:
            print ("Found ip %s in subnet %s" % (ip, matching))
            status = True
        if ip in blacklist_ips:
            print ("IP %s is individually blocked" % ip)
            status = True
    return status



ips = []
for line in sys.stdin:
    line = line.strip()
    if line:
        ips.append(line)

subnets = []
blacklist_ips = set()
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
                    else:
                        blacklist_ips.add(s)

if check_ips(ips):
    sys.exit(1)
