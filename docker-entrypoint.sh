#!/bin/sh

python3 -m get_robot_trigger
/bin/sh -c "sleep 3"
curl -s -X POST localhost:10001/quitquitquit
