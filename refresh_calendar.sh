#!/bin/bash

pythonscript="/home/ubuntu/workspace/soe-event-scraper/soe_events.py"
logout="/home/ubuntu/workspace/soe-event-scraper/logs/log.out"
logerr="/home/ubuntu/workspace/soe-event-scraper/logs/log.err"

$pythonscript >>$logout 2>>$logerr
cat $logout
cat $logerr
