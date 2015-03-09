#!/bin/bash

#
#   Schedule in crontab with:
#   0 0 * * * /home/ubuntu/workspace/soe-event-scraper/refresh_calendar.sh
#

pythonscript="/home/ubuntu/workspace/soe-event-scraper/soe_events.py"
logout="/home/ubuntu/workspace/soe-event-scraper/logs/log.out"
logerr="/home/ubuntu/workspace/soe-event-scraper/logs/log.err"

$pythonscript >>$logout 2>>$logerr
echo "Wrote logs to $logout and $logerr"
