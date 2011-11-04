#Copyright (c) 2010 Erik Cederstrand <erik@cederstrand.dk>.
#
#All rights reserved.
#
#Redistribution and use in source and binary forms, with or without modification, are
#permitted provided that the following conditions are met:
#
#   1. Redistributions of source code must retain the above copyright notice, this list of
#      conditions and the following disclaimer.
#
#   2. Redistributions in binary form must reproduce the above copyright notice, this list
#      of conditions and the following disclaimer in the documentation and/or other materials
#      provided with the distribution.
#
#THIS SOFTWARE IS PROVIDED BY <COPYRIGHT HOLDER> ``AS IS'' AND ANY EXPRESS OR IMPLIED
#WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
#FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> OR
#CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
#CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
#SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
#ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
#NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
#ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

'''This module provides an interface for comunicating with a Microsoft
Exchange 2007/2010 Server with Exchange Web Services (EWS) support. It
currently only implements functions for adding, finding and deleting 
calendar items.'''

from suds import WebFault
from suds.client import Client
from suds.sax.element import Element
from suds.transport.https import WindowsHttpAuthenticated
from suds.transport.https import HttpAuthenticated
from ntlm import HTTPNtlmAuthHandler
import urllib2
import logging
from datetime import datetime
from os import makedirs
import shutil
from copy import deepcopy
from xml.etree import ElementTree

class Exchange:
    '''Provides an interface for an Exchange server.'''

    def __init__(self, domain, username, password, datadir, protocol='https', \
            authtype=None, debug=False):

        self.domain = domain
        self.protocol = protocol
        self.urlprefix = '%s://%s/EWS' % (protocol, domain)
        self.wsdl = '%s/Services.wsdl' % self.urlprefix

        self.credentials = self.Credentials(username, password)
        self.transport = self.Transport(self, authtype)

        self.localdir = '%s/%s' % (datadir, domain)
        
        # Download and fix up the WSDL
        localwsdl = 'file://%s' % self.setup()

        authtype = self.transport.authtype
        if authtype == self.transport.NTLM:
            auth = WindowsHttpAuthenticated(username=username, password=password)
        elif authtype == self.transport.Basic:
            auth = HttpAuthenticated(username=username, password=password)
        else:
            raise Exception('Auth type not supported by Client(): %s' % authtype)

        if debug:
            logging.basicConfig(level=logging.INFO)
            logging.getLogger('suds.client').setLevel(logging.DEBUG)
            self.client = Client(url=localwsdl, transport=auth, cache=None)
        else:
            self.client = Client(url=localwsdl, transport=auth, cachingpolicy=1)
            self.client.options.cache.setduration(weeks=1)

        self.version = self.Version(self)
        self.calendar = self.Calendar(self)


    def __str__(self):
        ver = self.version
        return '''Location: %s://%s
Version: %s
Name (according to XSD): %s
Name (according to build numbers): %s
Build: %s
Auth type: %s''' % (self.protocol, self.domain, ver.name, ver.shortname, \
            ver.realshortname, ver.build, self.transport.authtype)


    def setup(self):
        '''Patches the WSDL file to include a service tag. Returns path to
        local WSDL file.'''
        trans = self.transport
        try:
            makedirs(self.localdir)
        except OSError:
            # Directory already exists
            pass

        # Download messags.xsd file
        messages_url = '%s/messages.xsd' % self.urlprefix
        with open('%s/%s' % (self.localdir, 'messages.xsd'), 'w') as msg_xsd:
            msg_xsd.write(trans.geturl(messages_url, trans.authtype))

        # Download types.xsd file
        types_url = '%s/types.xsd' % self.urlprefix
        with open('%s/%s' % (self.localdir, 'types.xsd'), 'w') as types_xsd:
            types_xsd.write(trans.geturl(types_url, trans.authtype))

        # Modify WSDL to add service description
        service_url = '%s/Exchange.asmx' % self.urlprefix
        servicexml = '''  <wsdl:service name="ExchangeServices">
    <wsdl:port name="ExchangeServicePort" binding="tns:ExchangeServiceBinding">
      <soap:address location="%s"/>
    </wsdl:port>
  </wsdl:service>
</wsdl:definitions>''' % service_url
        localwsdl = '%s/%s' % (self.localdir, 'Services.wsdl')
        wsdlxml = trans.geturl(self.wsdl, trans.authtype)
        with open(localwsdl, 'w') as wsdl:
            wsdl.write(wsdlxml.replace('</wsdl:definitions>', servicexml))

        return localwsdl


    class Version:
        '''Holds information about the server version'''

        def __init__(self, exchange):
            self.exchange = exchange
            self.shortname, self.majorversion, self.minorversion, self.majorbuildnumber, \
                self.minorbuildnumber = self.get()

            # Major versions below 8 don't support EWS, so we would never be
            # able to talk to such a server. This table is according to 
            # official Microsoft docs.

            # 'shortname' is what's used in SOAP request headers when talking 
            # to the server. It comes from types.xsd. 'realshortname' is the
            # official name corresponding to the version numbers supplied 
            # in SOAP response headers. For some unknown reason, they may
            # differ.
            versiondict = {\
             '8': {\
              '0': ('Exchange2007','Microsoft Exchange Server 2007'),\
              '1': ('Exchange2007_SP1','Microsoft Exchange Server 2007 SP1'),\
              '2': ('Exchange2007_SP2','Microsoft Exchange Server 2007 SP2') \
             },\
             '14': {\
              '00': ('Exchange2010','Microsoft Exchange Server 2010'),\
              '01': ('Exchange2010_SP1','Microsoft Exchange Server 2010 SP1'),\
              '02': ('Exchange2010_SP2','Microsoft Exchange Server 2010 SP2') \
             }\
            }

            if versiondict.has_key(self.majorversion) and\
               versiondict[self.majorversion].has_key(self.minorversion):
                self.realshortname, self.name = \
                    versiondict[self.majorversion][self.minorversion]
            else:
                raise Exception('Unknown Exchange version. I know the \
                    following: %s' % versiondict)
            
            self.build = '%s.%s.%s.%s' % (self.majorversion, self.minorversion, \
            self.majorbuildnumber, self.minorbuildnumber)


        def get(self):
            '''Tries to get ask the server which version it has. We haven't 
            set up the Calendar object yet, so just generate an empty request.
            We only need a response header containing a ServerVersionInfo 
            element. Apparently, Exchange has no problem supplying one version 
            in its types.xsd and reporting another in its SOAP headers. Use the 
            types.xsd version in SOAP requests.'''
            
            # The URL of the EWS service
            url = '%s/Exchange.asmx' % self.exchange.urlprefix
            
            # We already know the auth type used
            trans = self.exchange.transport
            authtype = trans.authtype

            # Get the server version from types.xsd. A server response provides
            # the build numbers.
            types_xsd = '%s/%s' % (self.exchange.localdir, 'types.xsd')
            shortname = ElementTree.parse(types_xsd).getroot().attrib['version']
            
            # I'm lazy. Just generate enough to get a soap:Header response
            xml = self.exchange.transport.wrap('<m:FindItem/>', shortname)
            try:
                # urllib2 might decide to throw an error on the response. We
                # don't care, we just want the raw data.
                response = trans.geturl(url=url, authtype=authtype, data=xml)
            except urllib2.HTTPError as e:
                response = e.read()

            soapns = 'http://schemas.xmlsoap.org/soap/envelope/'
            tns = 'http://schemas.microsoft.com/exchange/services/2006/types'
            header = ElementTree.fromstring(response).find('{%s}Header' % soapns)
            info = header.find('{%s}ServerVersionInfo' % tns).attrib
            if not info:
                raise Exception('No versioninfo in response: %s' % response)
            
            majorv = info['MajorVersion']
            minorv = info['MinorVersion']
            majorb = info['MajorBuildNumber']
            minorb = info['MinorBuildNumber']
            return shortname, majorv, minorv, majorb, minorb

        def __str__(self):
            return '%s.%s.%s.%s (%s)' % (self.majorversion, self.minorversion, \
                self.majorbuildnumber, self.minorbuildnumber, self.name)


    class Transport:
        '''Autoconfigures and stores information on the auth type of the
        server.'''

        def __init__(self, exchange, authtype=None):
            # Authentication method enums
            self.NTLM = 'NTLM'
            self.Basic = 'basic'
            self.Digest = 'digest'
            self.exchange = exchange

            if authtype:
                self.authtype = authtype
            else:
                self.authtype = self.gettype()


        def test(self):
            '''Tests the connection to the server.'''
            if self.gettype():
                return True


        def _isxml(self, txt):
            '''Helper function. Test if response is an XML doc'''
            if txt[0:5] == '<?xml':
                return True
            return False


        def _isunauthorized(self, txt):
            '''Helper funciton. Test if response contains an "Unauthorized"
            message'''
            if txt.lower().find('unauthorized') >= 0:
                return True
            return False


        def geturl(self, url, authtype, data=None):
            '''Downloads a file using the specified auth type'''
            passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
            cred = self.exchange.credentials
            passman.add_password(None, url, cred.username, cred.password)

            # Create authentication handler
            if authtype is self.NTLM:
                handler = HTTPNtlmAuthHandler.HTTPNtlmAuthHandler(passman)
            elif authtype is self.Basic:
                handler = urllib2.HTTPBasicAuthHandler(passman)
            elif authtype is self.Digest:
                handler = urllib2.HTTPDigestAuthHandler(passman)
            else:
                raise Exception('Unknown authtype')

            https = urllib2.HTTPSHandler()
            opener = urllib2.build_opener(https, handler)
            urllib2.install_opener(opener)

            # Retrieve the result
            fp = urllib2.urlopen(url, data)
            return fp.read()

        
        def gettype(self):
            '''Downloads the WSDL file to try to determine the auth type the
            server uses'''
            url = self.exchange.wsdl

            passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
            cred = self.exchange.credentials
            passman.add_password(None, self.exchange.domain, cred.username, \
                cred.password)

            # Create authentication handlers
            auth_NTLM = HTTPNtlmAuthHandler.HTTPNtlmAuthHandler(passman)
            auth_NTLM.type = self.NTLM
            auth_basic = urllib2.HTTPBasicAuthHandler(passman)
            auth_basic.type = self.Basic
            auth_digest = urllib2.HTTPDigestAuthHandler(passman)
            auth_digest.type = self.Digest

            https = urllib2.HTTPSHandler()
            # create and install the opener
            for handler in (auth_basic, auth_NTLM, auth_digest):
                opener = urllib2.build_opener(https, handler)
                urllib2.install_opener(opener)

                # Retrieve the result. We allow 401 errors to happen since
                #the authentication type may be wrong, giving a 401 response.
                try:
                    fp = urllib2.urlopen(url)
                    response = fp.read()
                    if self._isxml(response):
                        return handler.type
                    elif self._isunauthorized(response):
                        # Exchange brilliantly sends an unauth message as a
                        # non-401 page
                        raise urllib2.HTTPError(url, 401, 'Unauthorized', \
                            None, fp)
                    else:
                        raise Exception('Unknown response from Exchange:\n\n%s'\
                            % response)
                except urllib2.HTTPError as e:
                    if e.code != 401:
                        raise e

            # All auth methods give a 401 error, so the credentials must be
            # wrong
            raise urllib2.HTTPError(url, '401', 'Unauthorized', None, fp)


        def wrap(self, xml, shortname=None):
            '''Generate the necessary boilerplate XML for a raw SOAP request.
            The XML is specific to the server version.'''
            if shortname is None:
                shortname = self.exchange.version.shortname
            header = Element('t:RequestServerVersion')
            header.set('Version', shortname)
            return '''<?xml version="1.0" encoding="UTF-8"?>
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" xmlns:t="http://schemas.microsoft.com/exchange/services/2006/types" xmlns:m="http://schemas.microsoft.com/exchange/services/2006/messages">
<s:Header>%s</s:Header>
<s:Body>%s</s:Body>
</s:Envelope>''' % (header, xml)


    class Credentials:
        '''Keeps login info'''

        def __init__(self, username, password):
            self.username = username
            self.password = password


    class Calendar:
        '''An interface for the Exchange calendar'''

        def __init__(self, exchange):
            # Enums
            self.IdOnly = 'IdOnly'
            self.AllProperties = 'AllProperties'

            self.exchange = exchange
            self.client = exchange.client
            self.credentials = exchange.credentials


        def _restriction(self, operator, field, value):
            '''Build a restriction XML subtree'''

            uri = Element('t:FieldURI')
            uri.set('FieldURI', field)
            val = Element('t:Constant')
            val.set('Value', value)

            if   operator == '==':
                op = Element('t:IsEqualTo')
            elif operator == '!=':
                op = Element('t:IsNotEqualTo')
            elif operator == '>':
                op = Element('t:IsGreaterThan')
            elif operator == '<':
                op = Element('t:IsLessThan')
            elif operator == '<=':
                op = Element('t:IsLessThanOrEqualTo')
            elif operator == '>=':
                op = Element('t:IsGreaterThanOrEqualTo')
            elif operator == 'contains':
                op = Element('t:Contains')
                op.set('ContainmentMode', 'Substring')
                op.set('ContainmentComparison', 'Exact')
                op.append(uri)
                op.append(val)
                return op
            else:
                raise Exception('Operator not supported')

            op.append(uri)
            const = Element('t:FieldURIOrConstant')
            const.append(val)
            op.append(const)
            return op


        def getitems(self, account, startdate=None, enddate=None, \
                categories=None, shape=None):
            '''Gets all items within an account, optionally restricted by
            start- and enddates and a list of categories'''

            if shape is None:
                shape = self.IdOnly

            finditem = Element('m:FindItem')
            finditem.set('Traversal', 'Shallow')

            itemshape = Element('m:ItemShape')
            baseshape = Element('t:BaseShape').setText(shape)
            itemshape.append(baseshape)
            if categories:
                additionalproperties = Element('t:AdditionalProperties')
                fielduri = Element('t:FieldURI')
                fielduri.set('FieldURI', 'item:Categories')
                additionalproperties.append(fielduri)
                itemshape.append(additionalproperties)
            finditem.append(itemshape)

            def _notnone(var):
                '''Helper function for map()'''
                return var is not None

            nres = sum(map(int, map(_notnone, (startdate, enddate, \
                categories))))
            if nres >= 1:
                res = Element('m:Restriction')
            if nres == 1:
                restriction = res
            elif nres > 1:
                restriction = Element('t:And')
            if categories:
                if len(categories) == 1:
                    restriction.append(self._restriction('contains', \
                        'item:Categories', categories[0]))
                else:
                    ortype = Element('t:Or')
                    for cat in categories:
                        ortype.append(self._restriction('contains', \
                            'item:Categories', cat))
                    restriction.append(ortype)
            if startdate:
                restriction.append(self._restriction('>=', 'calendar:Start', \
                    startdate.ewsformat()))
            if enddate:
                restriction.append(self._restriction('<=', 'calendar:End', \
                    enddate.ewsformat()))

            if nres > 1:
                res.append(restriction)
            finditem.append(res)

            distinguishedfolderid = Element('t:DistinguishedFolderId')
            distinguishedfolderid.set('Id', 'calendar')
            parentfolderids = Element('m:ParentFolderIds')
            mailbox = Element('t:Mailbox')
            emailaddress = Element('t:EmailAddress').setText(account)
            mailbox.append(emailaddress)
            distinguishedfolderid.append(mailbox)
            parentfolderids.append(distinguishedfolderid)
            finditem.append(parentfolderids)

            xml = self.exchange.transport.wrap(finditem)

            try:
                result = self.client.service.FindItem(__inject={'msg':xml})
            except WebFault as e:
                raise e

            msg = result.FindItemResponseMessage
            rspclass = msg._ResponseClass
            rspcode = msg.ResponseCode
            if rspclass == 'Error':
                raise Exception('Error code: %s message: %s' % \
                    (rspcode, msg.MessageText))
            if rspclass != 'Success':
                raise Exception('Unknown response class: %s code: %s' % \
                    (rspclass, rspcode))

            if rspcode != 'NoError':
                raise Exception('Unknown response code: %s' % rspcode)
            if not msg.RootFolder._IncludesLastItemInRange:
                raise Exception('Not all items were transferred')
            if msg.RootFolder._TotalItemsInView == 0:
                return []

            if type(msg.RootFolder.Items[0]).__name__ == 'list':
                fullitems = msg.RootFolder.Items[0]
            else:
                # Only one item returned
                fullitems = [msg.RootFolder.Items.CalendarItem]

            if not categories:
                return fullitems

            # Filter for category. Searching for categories only works with
            # 'Or' operator, so we need to ignore items with only some
            # but not all categories present.
            items = []
            for item in fullitems:
                itemcats = item.Categories[0]
                if set(categories).issubset(set(itemcats)):
                    items.append(item)
            return items


        def delitems(self, ids):
    
            
            '''Takes a list of (id, changekey) tuples. Returns result of
            deletion as a list of tuples (success[True|False], errormessage),
            in the same sequence as the input list.'''

            status = []
            if not ids:
                # Nothing to do
                return status

            deleteitem = Element('m:DeleteItem')
            deleteitem.set('DeleteType', 'HardDelete')
            deleteitem.set('SendMeetingCancellations', 'SendToNone')

            itemids = Element('m:ItemIds')
            itemid = Element('t:ItemId')

            # copy.deepcopy() is an order of magnitude faster than having
            # Element() inside the loop. It matters because 'ids' may
            # be a very large list.
            for iid, changekey in ids:
                i = deepcopy(itemid)
                i.set('Id', iid)
                i.set('ChangeKey', changekey)
                itemids.append(i)
            deleteitem.append(itemids)

            xml = self.exchange.transport.wrap(deleteitem)

            try:
                result = self.client.service.DeleteItem(__inject={'msg':xml})
            except WebFault as e:
                raise e

            # Result may come as a single object or a list of objects
            if type(result.DeleteItemResponseMessage).__name__ == 'list':
                msgs = result.DeleteItemResponseMessage
            else:
                msgs = [result.DeleteItemResponseMessage]
            msglen = len(msgs)
            if len(msgs) != len(ids):
                raise Exception('Returned response count doesn\'t match: \
                    got %s, expected %s' % (len(msgs), len(ids)))
            for msg in msgs:
                rspclass = msg._ResponseClass
                rspcode = msg.ResponseCode
                if rspclass == 'Error':
                    if rspcode == 'ErrorItemNotFound':
                        # Should not happen, so don't worry about performance
                        status.append( (False, '%s: %s' % ( msg.MessageText, \
                            ids[len(status)] ) ) )
                        continue
                    raise Exception('Error code: %s message: %s' % \
                        (rspcode, msg.MessageText))
                if rspclass != 'Success':
                    raise Exception('Unknown response class: %s code: %s' % \
                        (rspclass, rspcode))

                if not rspcode == 'NoError':
                    raise Exception('Unknown response code: %s' % rspcode)
                status.append((True, None))

            return status


        def getids(self, items):
            '''Takes a list of items with full or partial properties as
            produced from getitems() and returns a list of (id, changekey)
            tuples.'''
            idlist = []
            for item in [i.ItemId for i in items]:
                idlist.append((item._Id, item._ChangeKey))
            return idlist


        class Item:
            '''Models a calendar item'''

            def __init__(self, subject, start, end, body=None, location=None, \
                    hasreminder=False):
                self.subject = subject
                self.start = start
                self.end = end
                self.body = body
                self.location = location
                self.hasreminder = hasreminder

            def __str__(self):
                return '''Subject: %s
Start: %s
End: %s
Location: %s
Body: %s''' % (self.subject, self.start, self.end, self.location, self.body)


        def additems(self, account, items, categories):
            '''Creates new items in the calendar. 'items' is a list of  Item
            objects. Returns a list of (id, changekey) tuples in the same
            order as the input.'''

            status = []
            if not items:
                return status

            createitem = Element('m:CreateItem')
            createitem.set('SendMeetingInvitations', 'SendToNone')

            saveditemfolderid = Element('m:SavedItemFolderId')
            distinguishedfolderid = Element('t:DistinguishedFolderId')
            distinguishedfolderid.set('Id', 'calendar')
            mailbox = Element('t:Mailbox')
            emailaddress = Element('t:EmailAddress').setText(account)
            mailbox.append(emailaddress)
            distinguishedfolderid.append(mailbox)
            saveditemfolderid.append(distinguishedfolderid)
            createitem.append(saveditemfolderid)

            calitems = Element('m:Items')

            # Prepare objects for CalendarItem creation
            calitem = Element('t:CalendarItem')
            subject = Element('t:Subject')
            body = Element('t:Body')
            body.set('BodyType', 'Text')
            cats = None
            if categories:
                cats = Element('t:Categories')
                for cat in categories:
                    cats.append(Element('t:String').setText(cat))
            reminder = Element('t:ReminderIsSet')
            start = Element('t:Start')
            end = Element('t:End')
            busystatus = Element('t:LegacyFreeBusyStatus').setText('Busy')
            location = Element('t:Location')

            # Using copy.deepcopy() increases performance drastically on large arrays
            for item in items:
                i = deepcopy(calitem)
                i.append(deepcopy(subject).setText(item.subject))
                if item.body:
                    i.append(deepcopy(body).setText(item.body))
                if cats:
                    i.append(cats)
                i.append(deepcopy(reminder).setText(int(item.hasreminder)))
                i.append(deepcopy(start).setText(item.start.ewsformat()))
                i.append(deepcopy(end).setText(item.end.ewsformat()))
                i.append(busystatus)
                if item.location:
                    i.append(deepcopy(location).setText(item.location))
                calitems.append(i)

            createitem.append(calitems)
            xml = self.exchange.transport.wrap(createitem)
            try:
                result = self.client.service.CreateItem(__inject={'msg':xml})
            except WebFault as e:
                raise e

            # Result may come as a single object or a list of objects
            if type(result.CreateItemResponseMessage).__name__ == 'list':
                msgs = result.CreateItemResponseMessage
            else:
                msgs = [result.CreateItemResponseMessage]
            if len(msgs) != len(items):
                raise Exception('Returned response count doesn\'t match: \
                    got %s, expected %s' % (len(msgs), len(items)))

            idlist = []
            for msg in msgs:
                rspclass = msg._ResponseClass
                rspcode = msg.ResponseCode
                if rspclass == 'Error':
                    raise Exception('Error code: %s message: %s' % \
                        (rspcode, msg.MessageText))
                if rspclass != 'Success':
                    raise Exception('Unknown response class: %s code: %s' % \
                        (rspclass, rspcode))

                if rspcode != 'NoError':
                    raise Exception('Unknown response code: %s' % rspcode)

                item = msg.Items.CalendarItem.ItemId
                idlist.append((item._Id, item._ChangeKey))

            return idlist


class EWSDateTime(datetime):
    '''Extends the normal datetime implementation to satisfy Exchange'''

    def ewsformat(self):
        '''ISO 8601 format to satisfy xs:datetime as interpreted by Exchange'''
        return self.strftime('%Y-%m-%dT%H:%M:%SZ')

