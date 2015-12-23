# SOE Event Scraper

Program to create an icalendar feed from events listed UCSC's engineering department website.


## Overview

Project that regularly gets information from [https://www.soe.ucsc.edu/events](https://www.soe.ucsc.edu/events) and updates an icalendar feed to allow automatic updates to Google Calendar. There is an option to make the scraping selective; only events with non-empty descriptions will then be included in the feed to keep the feed concise.

_soe\_events.py_ is the Python script that does all the real work.

_refresh\_calendar.sh_ specifies logging to keep the cron listing simple.
