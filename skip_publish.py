#!/usr/bin/env python3
"""
Simple script to grab every Nth line of input and
publish to an MQTT broker.

"""
import sys
import os

count=0
max=20
hostname=os.uname()[1]

for line in sys.stdin:
    if count == 0:
        cmd = "mosquitto_pub -h mqtt -t HA/"+hostname+"/mobile/air_quality -m '"+line.strip()+"'"
        os.system(cmd)
    count += 1
    if count == max:
        count=0
 