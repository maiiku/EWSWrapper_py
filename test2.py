# -*- coding: utf-8 -*-
'''Shows some of the functions available in the Exchange module'''

from EWSWrapper import EWSWrapper, EWSDateTime

domain  = 'red002.mail.emea.microsoftonline.com'
user    = 'crm@dknotus.pl'
pw      = 'Haslo66!'

ews = EWSWrapper(host=domain, username=user, password=pw).wrapper

account = 'michal.korzeniowski@dknotus.pl'

start = EWSDateTime(2011, 10, 1, 13, 37, 0)
end = EWSDateTime(2011, 10, 20, 14, 0, 0)

to_do = 'calendar_list'

if to_do == 'calendar_add':
    items = ews.addCalendarEvent(subject='Halo z pythona 2', \
                                 body='haloooooooooo', \
                                 start=start, \
                                 end=end, \
                                 attendees=[account], \
                                 on_behalf=account, \
                                 location='Mars')
    print '\nreturned IDs:'
    for i in items:
        print i
elif to_do == 'calendar_edit':
    items = ews.editCalendarEvent(id='AAMkAGRkNzBkYTNlLTg2NjEtNDA5YS1iOWU3LTY0YWRhZTYzMmUwMgBGAAAAAABVA5BhgjxARYSIPL1mPSAUBwAYjaWDBdsHQo5pvIdFf3S+AAAEQYWyAAAYjaWDBdsHQo5pvIdFf3S+AB9cBhZxAAA=', \
                                  ckey='DwAAABYAAAAYjaWDBdsHQo5pvIdFf3S+AB9cCr7N',\
                                  attendees=[account], \
                                  location='Mars')
    print '\nreturned IDs:'
    for i in items:
        print i   
elif to_do == 'calendar_list':
    items = ews.listCalendarEvent(on_behalf=account, \
                                  start=start, \
                                  end=end, \
                                  shape='DEFAULT_PROPERTIES')
    print '\nreturned IDs:'
    for i in items:
        print i    
elif to_do == 'calendar_delete':
    items = ews.deleteCalendarEvent(['AAMkAGRkNzBkYTNlLTg2NjEtNDA5YS1iOWU3LTY0YWRhZTYzMmUwMgBGAAAAAABVA5BhgjxARYSIPL1mPSAUBwAYjaWDBdsHQo5pvIdFf3S+AAAEQYWyAAAYjaWDBdsHQo5pvIdFf3S+AB9cBhZxAAA='])
    print '\nResults:'
    for i in items:
        print i
if to_do == 'task_add':
    items = ews.addTask(subject='Task z pythona', \
                        body=u'Test dodawania tasków', \
                        due=end, \
                        reminderdue=start, \
                        on_behalf='arkadiusz.tarkiewicz@dknotus.pl')
    print '\nreturned IDs:'
    for i in items:
        print i
if to_do == 'task_edit':
    items = ews.editTask(id='AAMkADkzYjJmNWQ1LTNkYzctNDQxYy05ZTNkLWQ2MjBjOWU2MmU3OABGAAAAAABstM1IOqraQJ32b8x90xBiBwDYjN7FxXrWQpHh4zg87vHzAAAKWdwKAACFWm3OzBDcTYDUBCCa0OxUAAt88oSAAAA=', \
                         ckey='EwAAABYAAACFWm3OzBDcTYDUBCCa0OxUAAt88oyA', \
                         subject=u'Zaktualizowany Task', \
                         body=u'Test dodawania tasków', \
                         due=end, \
                         sensitivity='PERSONAL', \
                         reminderdue=start)
    print '\nreturned IDs:'
    for i in items:
        print i       
elif to_do == 'task_delete':
    items = ews.deleteTask(['AAMkAGRkNzBkYTNlLTg2NjEtNDA5YS1iOWU3LTY0YWRhZTYzMmUwMgBGAAAAAABVA5BhgjxARYSIPL1mPSAUBwAYjaWDBdsHQo5pvIdFf3S+AAAEQYW3AAAYjaWDBdsHQo5pvIdFf3S+AB9cDCcPAAA='])
    print '\nResults:'
    for i in items:
        print i
elif to_do == 'task_list':
    items = ews.listTask(on_behalf=account, \
                         end=start)
    print '\nreturned IDs:'
    for i in items:
        print i
elif to_do == 'folder_list':
    items = ews.listFolders(on_behalf=account, \
                         type='INBOX')
    print '\nreturned IDs:'
    for i in items:
        print i
#ids = cal.getids(items)
