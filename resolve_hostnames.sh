#!/bin/bash

while read line
do
    curl -s https://dns.google.com/resolve?name=$line | jq '.Answer[].data' | cut -d'"' -f2
done


