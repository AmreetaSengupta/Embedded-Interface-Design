#!/bin/bash

node node_server.js &
P1=$!
python3 sensor_reading_gui.py &
P2=$!
wait $P1 $P2
