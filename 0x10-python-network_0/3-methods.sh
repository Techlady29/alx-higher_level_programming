#!/bin/bash
# script that receives a URL and displays all HTTP methods the server will accept
curl -s -I -X OPTIONS "$1" | grep "ALLOW" | CUT -F2- -d" "
