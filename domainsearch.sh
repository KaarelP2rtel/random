#!/bin/bash

for domain  in {{0..9},{a..z}}{{0..9},{a..z}}; do
	url=${domain}.ee
	if nslookup  $url 2>1 >/dev/null; then
		echo "$url found with nslookup"	
	elif whois $url 2>1 | grep "not found" --quiet; then
		echo "$url IS AVAILABLE!!!!"
	else echo "$url is not avialable"
	fi
done

