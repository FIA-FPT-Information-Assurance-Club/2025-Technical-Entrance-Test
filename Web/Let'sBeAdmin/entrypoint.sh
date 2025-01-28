#!/bin/sh
set -e

trap 'kill -TERM $PID' TERM INT

./app --port 62233 &

PID=$!

wait $PID

trap - TERM INT
wait $PID
EXIT_STATUS=$?
exit $EXIT_STATUS