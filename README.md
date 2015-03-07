# SOE Event Scraper

Scripts to create an icalendar feed from events listed UCSC's engineering department website.


## Overview

Python and Bash scripts to regularly get information from [https://www.soe.ucsc.edu/events](https://www.soe.ucsc.edu/events) and update an icalendar feed to allow automatic updates to Google Calendar. A copy of the code will be deployed on my account on UCSC's servers, so anyone can subscribe to the feed using the link [http://people.ucsc.edu/~beran/calendar/soe.ics](http://people.ucsc.edu/~beran/calendar/soe.ics). The web scraping can be selective; it can be specified whether or not to include events that are listed without descriptions. This keeps the number of events in the feed very small, only including the most public-friendly ones. The feed at [http://people.ucsc.edu/~beran/calendar/soe.ics](http://people.ucsc.edu/~beran/calendar/soe.ics) will only include events with descriptions.
