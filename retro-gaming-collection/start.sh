#!/bin/bash

# Find the process ID (PID) using lsof
PID=$(/usr/bin/lsof -t -i:5000)

# Check if a PID was found
if [ -n "$PID" ]; then
    echo "Terminating process using port 5000 (PID: $PID)..."
    /bin/kill -9 $PID
    echo "Process terminated."
else
    echo "No process found on port 5000."
fi

python3 /var/www/vhosts/graememccall.com/httpdocs/retro-gaming-collection/src/app.py &