#!/bin/bash

while read line
do
    curl -s https://dns.google.com/resolve?name=$line | jq '.Answer[] | select (.type==1) | .data' | cut -d'"' -f2
done


