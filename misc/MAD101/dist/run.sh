#!/bin/sh

socat tcp-listen:1337,fork,reuseaddr,su=nobody EXEC:"python3 /server.py",stderr