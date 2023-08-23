#!/usr/bin/env python3
"""
Simple script to grab every Nth line of input and
publish to an MQTT broker.

"""
import sys
import os

count=0
max=3

for line in sys.stdin:
    if count == 0:
        print("count:", count)
        cmd = "mosquitto_pub -h polana -t test/topic -m '"+line+"'"
        os.system(cmd)
        count += 1
        if count == max:
            count=0
 