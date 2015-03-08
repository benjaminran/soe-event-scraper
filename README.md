# SOE Event Scraper

Scripts to create an icalendar feed from events listed UCSC's engineering department website.


## Overview

Python and Bash scripts to regularly get information from [https://www.soe.ucsc.edu/events](https://www.soe.ucsc.edu/events) and update an icalendar feed to allow automatic updates to Google Calendar. I will deploy this code on an Amazon EC2 instance so anyone can subscribe to the feed using the link [http://52.11.81.109/calendar/soe.ics](http://52.11.81.109/calendar/soe.ics). The web scraping can be selective; it can be specified whether or not to include events that are listed without descriptions. This keeps the number of events in the feed very small, only including the most public-friendly ones. The feed on my EC2 instance will only include events with descriptions.
