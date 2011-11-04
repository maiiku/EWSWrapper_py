# -*- coding: utf-8 -*-
'''Shows some of the functions available in the Exchange module'''

from EWSWrapper import EWSWrapper, EWSDateTime
import json
from django.http import HttpResponse
import random
import calendar
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
domain  = 'red002.mail.emea.microsoftonline.com'
user    = 'crm@dknotus.pl'
pw      = 'Haslo66!'

ews = EWSWrapper(host=domain, username=user, password=pw).wrapper

account = 'michal.korzeniowski@dknotus.pl'

def addEvent(CalendarStartTime, CalendarEndTime, CalendarTitle, IsAllDayEvent):
    pass

def listEvent(day, type):
    day = parse_date(day)
    if type=="month":
        st = EWSDateTime(int(day.strftime("%Y")),int(day.strftime("%m")),1,0,0,0)
        ed = EWSDateTime(int(day.strftime("%Y")),int(day.strftime("%m")),calendar.monthrange(int(day.strftime("%Y")), int(day.strftime("%m")))[1],23,59,59,)
        cnt = 50
    if type=="week":
        monday = int(day.strftime("%d")) - int(day.strftime("%w")) if not 0 else 7 - 1
        st = EWSDateTime(int(day.strftime("%Y")),int(day.strftime("%m")),monday,0,0,0)
        ed = EWSDateTime(int(day.strftime("%Y")),int(day.strftime("%m")),monday+6,23,59,59)
        cnt = 20
    if type=="day":
        st = EWSDateTime(int(day.strftime("%Y")),int(day.strftime("%m")),int(day.strftime("%d")),0,0,0)
        ed = EWSDateTime(int(day.strftime("%Y")),int(day.strftime("%m")),int(day.strftime("%d")),23,59,59)
        cnt = 20
    return listEventByRange(st, ed, cnt)

def listEventByRange(st, ed, cnt):
    ret = {'events' : [],
           "issort" : True,
           "start"  : format_date(st),
           "end"    : format_date(ed),
           "error"  : None
    }
    items = ews.listCalendarEvent(start=st, end=ed, on_behalf=account)
    for item in items:
        ret["events"].extend([[item.ItemId._Id, 
                           item.Subject, 
                           format_date(item.Start), 
                           format_date(item.End), 
                           0, #is spans over 24h 
                           0, #allday, 
                           random.randint(-1,13), 
                           1, #editable 
                           item.Location, 
                           (", ".join("%s" % (j) for j in [mialbox.Mailbox.Name for mialbox in item.RequiredAttendees.Attendee])) if item.RequiredAttendees else None
                      ]])
        
    return ret


def parse_date(datestr):
    date_parts = datestr.split(" ")
    if "/" in date_parts[0]:
        date_parts_date = date_parts[0].split("/")
        year = date_parts_date[0]
        month = date_parts_date[1]
        day = date_parts_date[2]
    elif ":" in date_parts[0]:
        date_parts_time = date_parts[0].split(":")
        hour = date_parts_time[0]
        minute = date_parts_time[1]
    if(len(date_parts)>1):
        if ":" in date_parts[1]:
            date_parts_time = date_parts[1].split(":")
            hour = date_parts_time[0]
            minute = date_parts_time[1]
    try:
        return EWSDateTime(int(year), int(month), int(day), int(hour), int(minute), 0)
    except NameError:
        return EWSDateTime(0, 0, 0, int(hour), int(minute), 0)

def format_date(dateobj):
    return dateobj.strftime("%d/%m/%Y %H:%M")
    

def fromExDate(datestr):
    date_parts = datestr.replace(":", " ").replace("-", " ")
    date_parts = date_parts.split(" ");
    return EWSDateTime(date_parts[0], date_parts[1],date_parts[2], date_parts[3], date_parts[4], date_parts[5])
    

def viewheader(request):
    out = HttpResponse(request,
        mimetype="text/javascript",
        status="302",
        content_type="text/javascript;charset=UTF-8"
        )
    return out

def getCalendarList():
    #method = request.GET["method"]
    method = "list"
    
    if method == "list":
        result = listEvent("2011/10/25 00:00", "month")
        
    result = viewheader(json.dumps(result))
    print result