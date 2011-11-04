#!/usr/local/bin/python
'''Shows some of the functions available in the Exchange module'''

from Exchange import Exchange, EWSDateTime

datadir = 'wsdl'
domain = 'red002.mail.emea.microsoftonline.com'
user = 'crm@dknotus.pl'
pw = 'Haslo55!'

exchange = Exchange(domain=domain, username=user, password=pw, datadir=datadir)
print exchange

cal = exchange.calendar

account = 'michal.korzeniowski@dknotus.pl'
# Creates and gets items with both item categories present. This is great for 
# leaving other items alone when testing.
categories = ['Python', 'Suds']

calitems = []
print '\nItems to add:'
# These are UTC dates
start = EWSDateTime(2010, 07, 15, 16, 0, 0)
end = EWSDateTime(2010, 07, 15, 17, 0, 0)
# Build a list of items to create
for i in range(1, 6):
    item = cal.Item(subject='Test %s' % i, start=start, end=end, \
        body='Hi from Python', location='devnull')
    print '\n%s' % item
    calitems.append(item)

# Create the items we just made
ids = cal.additems(account=account, items=calitems, categories=categories)
print "\nAdded IDs:"
for i in ids:
    print i

# Search for the items we just created
start = EWSDateTime(2010, 07, 15, 16, 0, 0)
end = EWSDateTime(2010, 07, 15, 17, 0, 0)
items = cal.getitems(account=account, startdate=start, enddate=end, \
    categories=categories, shape=cal.IdOnly)
ids = cal.getids(items)
print '\nIDs of returned items:'
for i in ids:
    print i

# Delete the found items
result = cal.delitems(ids)
print '\nResult of deletion:'
for res in result:
    print res[0]
