#!/bin/bash

# Start the first process
npm run start &

sleep 5m

# Start the second process
npm run console

# Wait for any process to exit
wait -n

# Exit with status of process that exited first
exit $?