#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
from xml.dom.minidom import parseString
from icalendar import Calendar, Event
from datetime import datetime, timedelta
from pytz import timezone # timezone
import pytz
import time
from time import mktime


####    Options
DISCRIMINATE_SUMMARIES = True # require non-empty summary?


####    Script constants/variables
BASE_URL = "https://www.soe.ucsc.edu"
CALENDAR_NAME = "/var/www/html/calendar/soe.ics"
UID = "benjaminran@soeevents"
calendar = None


####    Calendar creation/manipulation functions

def make_calendar():
    global calendar
    calendar = Calendar()
    calendar.add('prodid', 'bran//soeevents//python//')
    calendar.add('version', '2.0')
    calendar.add('method', 'PUBLISH')

def save_calendar():
    f = open(CALENDAR_NAME, 'wb')
    f.write(calendar.to_ical())
    f.close()
    print("Wrote calendar to " + CALENDAR_NAME)

def add_event(title, summary, start):
    end = start + timedelta(hours=1)
    event = Event()
    event.add('summary', title)
    event.add('dtstart', start)
    event.add('dtend', end)
    event.add('dtstamp', datetime.now())
    event.add('description', summary)
    event['uid'] = UID+datetime.now().strftime("%Y%m%d%H%M%S")
    global calendar
    calendar.add_component(event)


####    Web scraping functions

##      Scraping from page

def soup_to_event(soup, url):
    title = find_title(soup)
    abstract = find_abstract(soup)
    start_time = find_start_time(soup)
    if (title is None or start_time is None): return False
    summary = ""
    if DISCRIMINATE_SUMMARIES:
        if abstract is None: return False
        else: summary += abstract + "\n"
    summary += url
    add_event(title, summary, start_time)
    print(title)
    print(summary)
    print(start_time)
    print('\n')
    return True

def find_title(soup):
    title = soup.title.get_text().replace(" | Jack Baskin School of Engineering", "")
    if(title=="View" or title==" " or title=="" or "CANCELLED" in title): return None
    return title

def find_abstract(soup):
    reached_abstract = False;
    for par in soup.findAll("p", { "class" : "MsoNormal" }):
        if reached_abstract: # is element after "Abstract"
            return par.get_text()
        if par.get_text()=="Abstract": # is "Abstract"
            reached_abstract = True;
    return None

def find_start_time(soup):
    em = soup.find("em")
    if em is None: return None
    text = em.get_text()
    start = text.find(", ") + 2
    text = text[start:]
    end = text.find(" to")
    text = text[:end]
    start = time.strptime(text, "%B %d, %I:%M %p")
    return datetime(2015,start[1],start[2],start[3],start[4],0,tzinfo=pytz.timezone("US/Pacific"))


##      Navigation

def get_first_url():
    html = requests.get(BASE_URL+"/events").content
    soup = BeautifulSoup(html)
    firstevent = soup.find("li", { "class" : "soe-events-item" })
    return BASE_URL+firstevent.a["href"]

def read_event_recur(url):
    html = requests.get(url).content
    soup = BeautifulSoup(html)
    soup_to_event(soup, url)
    next = soup.find("td", { "class" : "next" })
    if(next is None): return None
    else: return read_event_recur(BASE_URL+next.a["href"])

##      Main
if __name__ == '__main__':
    make_calendar()
    read_event_recur(get_first_url())
    save_calendar()
