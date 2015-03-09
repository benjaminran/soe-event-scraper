# SOE Event Scraper

Scripts to create an icalendar feed from events listed UCSC's engineering department website.


## Overview

Python and Bash scripts to regularly get information from [https://www.soe.ucsc.edu/events](https://www.soe.ucsc.edu/events) and update an icalendar feed to allow automatic updates to Google Calendar. This code is deployed on an Amazon EC2 instance so anyone can subscribe to the feed using the link [http://52.11.81.109/calendar/soe.ics](http://52.11.81.109/calendar/soe.ics). The deployed code enables the option making the scraping selective; only events with non-empty descriptions are included in the feed to keep the feed concise and more public-friendly.
