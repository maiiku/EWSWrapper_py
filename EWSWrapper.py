'''
/* EWSWrapper_py
 * ====================================================
 * @author Michal Korzeniowski <mko_san@lafiel.net>
 * @version 0.2
 * @date 04-2012
 * @website http://ewswrapper.lafiel.net/
 * ====================================================
 * Desciption
 * Provides API wrapper for easy usage of Microsoft 
 * Exchange Web Services. EWSWrapper utilzes some
 * code written by Erik Cederstrand <erik@cederstrand.dk>
 * - Calendar events: add, update, delete, list, synch
 * - Taks	    : add, update, delete, list
 * - Messages	    : no support as of yet
 * - Folders	    : list, synch
 * 
 * ==================================================*/
'''
from suds import WebFault
from suds.client import Client
from suds.sax.element import Element
from suds.transport.https import WindowsHttpAuthenticated
from suds.transport.https import HttpAuthenticated
from suds import cache
from ntlm import HTTPNtlmAuthHandler
import urllib2
import logging
from datetime import datetime
from datetime import timedelta
from os import path
from copy import deepcopy
from xml.etree import ElementTree
import EWSType

class EWSWrapper:
    '''Provides an interface for an Exchange server.'''
    #Time Zone settings
    BaseOffset	    = "-P0DT1H0M0.0S"
    Offset	    = "-P0DT1H0M0.0S"
    DaylightTime    = "02:00:00.0000000"
    StandardOffset  = "P0DT0H0M0.0S"
    StandardTime    = "03:00:00.0000000"
    TimeZoneName    = "(GMT+01:00) Warsaw"
    TimeZoneId      = "Central European Standard Time"
    #for pagination purposes (search / sync)

    def __init__(self, host, username, password, datadir='wsdl', protocol='https', \
                 authtype=None, debug=False, timeArr=[]):

        self.host = host
        self.protocol = protocol
        self.urlprefix = '%s://%s/EWS' % (protocol, host)
        self.wsdl = '%s/Services.wsdl' % self.urlprefix

        self.credentials = self.Credentials(username, password)
        self.transport = self.Transport(self, authtype)

        #self.localdir = '%s/%s' % (datadir, host)

        # Download and fix up the WSDL
        #localwsdl = 'file://%s' % self.setup()
        basepath = ''
        basepath = path.normpath(path.dirname( path.realpath( __file__ )))
        self.basepath = basepath.replace('\\', '/') + '/' + datadir
        if self.basepath.startswith('/'):
            tmp_basepath = self.basepath[1:]
        else:
            tmp_basepath = self.basepath	
        localwsdl = 'file:///%s/services.wsdl' % (tmp_basepath)
        #cache path
        cachepath = basepath.replace('\\', '/') + '/suds_cache'


        #timezone settings
        if timeArr:
            self.BaseOffset	 = timeArr[BaseOffset] if BaseOffset in timeArr else self.BaseOffset
            self.Offset	         = timeArr[Offset] if Offset in timeArr else self.Offset	
            self.DaylightTime    = timeArr[DaylightTime] if DaylightTime in timeArr else self.DaylightTime
            self.StandardOffset  = timeArr[StandardOffset] if StandardOffset in timeArr else self.StandardOffset
            self.StandardTime    = timeArr[StandardTime] if StandardTime in timeArr else self.StandardTime
            self.TimeZoneName    = timeArr[TimeZoneName] if TimeZoneName in timeArr else self.TimeZoneName
            self.TimeZoneId      = timeArr[TimeZoneId] if TimeZoneId in timeArr else self.TimeZoneId

        authtype = self.transport.authtype
        if authtype == self.transport.NTLM:
            auth = WindowsHttpAuthenticated(username=username, password=password)
        elif authtype == self.transport.Basic:
            auth = HttpAuthenticated(username=username, password=password)
        else:
            raise Exception('Auth type not supported by Client(): %s' % authtype)
        
        #import jsonpickle
        #a = jsonpickle.encode(self)
        #h = open('/tmp/ews_ser.txt', 'w')
        #h.write(a)
        #h.close()
        
        if debug:
            #logging.basicConfig(level=logging.DEBUG, filename='/var/log/ews_debug.log',
            #        format='%(asctime)s %(levelname)s: %(message)s',
            #        datefmt='%Y-%m-%d %H:%M:%S')
            logging.getLogger('suds.client').setLevel(logging.DEBUG)
            the_cache = cache.FileCache(location=cachepath, days=0)
            self.client = Client(url=localwsdl, transport=auth, cache=the_cache)
        else:
            the_cache = cache.FileCache(location=cachepath, days=0)
            self.client = Client(url=localwsdl, transport=auth, cache=the_cache)
        self.version = self.Version(self)
        self.wrapper = self.Wrapper(self)

    class Version:
        '''Holds information about the server version'''

        def __init__(self, exchange):
            self.exchange = exchange
            self.shortname, self.majorversion, self.minorversion, self.majorbuildnumber, \
                self.minorbuildnumber = self.get()

            # Major versions below 8 don't support EWS, so we would never be
            # able to talk to such a server.

            # 'shortname' is what's used in SOAP request headers when talking 
            # to the server. It comes from types.xsd. 'realshortname' is the
            # official name corresponding to the version numbers supplied 
            # in SOAP response headers. For some unknown reason, they may
            # differ.
            versiondict = {\
                '8': {\
                    '0': ('Exchange2007','Microsoft Exchange Server 2007'),\
                    '1': ('Exchange2007_SP1','Microsoft Exchange Server 2007 SP1'),\
                    '2': ('Exchange2007_SP2','Microsoft Exchange Server 2007 SP2'), \
                    '3': ('Exchange2007_SP3','Microsoft Exchange Server 2007 SP3') \
                    },\
                '14': {\
                    '00': ('Exchange2010','Microsoft Exchange Server 2010'),\
                    '01': ('Exchange2010_SP1','Microsoft Exchange Server 2010 SP1'),\
                    '02': ('Exchange2010_SP2','Microsoft Exchange Server 2010 SP2'),\
                    '16': ('Exchange2010_SP2','Microsoft Exchange Server 2010 SP2') \
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
            types_xsd = '%s/%s' % (self.exchange.basepath, 'types.xsd')
            shortname = ElementTree.parse(types_xsd).getroot().attrib['version']

            # I'm lazy. Just generate enough to get a soap:Header response
            xml = self.exchange.transport.wrap('<m:FindItem Traversal="Shallow"><m:ItemShape><t:BaseShape>IdOnly</t:BaseShape></m:ItemShape>\
                                                <m:ParentFolderIds><t:DistinguishedFolderId Id="deleteditems"/></m:ParentFolderIds></m:FindItem>', shortname)
            try:
                # urllib2 might decide to throw an error on the response. We
                # don't care, we just want the raw data.
                response = trans.geturl(url=url, authtype=authtype, data=xml)
            except urllib2.HTTPError as e:
                response = e.read()
            #print response
            #import jsonpickle
            #a = jsonpickle.encode(response)
            #h = open('/tmp/ews_ser.txt', 'w')
            #h.write(a)
            #h.close()            
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
            '''Helper function. Test if response contains an "Unauthorized"
            message'''
            return 'unauthorized' in txt.lower()


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
            headers = {'Content-Type': 'text/xml; charset=utf-8'}
            req = urllib2.Request(url, data, headers)
            fp = urllib2.urlopen(req)
            return fp.read()


        def gettype(self):
            '''Downloads the WSDL file to try to determine the auth type the
            server uses'''
            url = self.exchange.wsdl

            passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
            cred = self.exchange.credentials
            passman.add_password(None, self.exchange.host, cred.username, \
                                 cred.password)

            # Create authentication handlers
            auth_NTLM = HTTPNtlmAuthHandler.HTTPNtlmAuthHandler(passman)
            auth_NTLM.type = self.NTLM
            auth_basic = urllib2.HTTPBasicAuthHandler(passman)
            auth_basic.type = self.Basic
            auth_digest = urllib2.HTTPDigestAuthHandler(passman)
            auth_digest.type = self.Digest

            https = urllib2.HTTPSHandler()
            fp = None
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
        
        def getTZ(self):
            # The URL of the EWS service
            url = '%s/Exchange.asmx' % self.exchange.urlprefix

            # Get the server version from types.xsd. A server response provides
            # the build numbers.
            types_xsd = '%s/%s' % (self.exchange.basepath, 'types.xsd')
            shortname = ElementTree.parse(types_xsd).getroot().attrib['version']

            # generate xml for timezones
            xml = self.wrap('<m:GetServerTimeZones ReturnFullTimeZoneData="false"></m:GetServerTimeZones>')
            response = self.geturl(url=url, authtype=self.authtype, data=xml)
            handle1=open('timezones.xml','w+')
            handle1.write(response)
            handle1.close()
            
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


    class Wrapper:
        '''EWSWrapper functions'''
        hasMoreItems    = False
        synchState      = None
        

        def __init__(self, exchange):
            # Enums
            self.types = EWSType.EWSType

            self.exchange = exchange
            self.client = exchange.client
            self.credentials = exchange.credentials

        def _restriction(self, operator, field, value, extended = False):
            '''Helper function to build retriction call'''

            if not extended:
                uri = Element('t:FieldURI')
                uri.set('FieldURI', field)
            else:
                uri = field
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

        def _mapi_reference(self, property_id, property_type, set_id):
            '''construct a mapi field reference'''
            path = Element('t:ExtendedFieldURI')
            path.set('DistinguishedPropertySetId', set_id)
            path.set('PropertyId', property_id)
            path.set('PropertyType', property_type)
            return path	    

        def listCalendarEvent(self, id=None, start=None, end=None, on_behalf=None, shape='DEFAULT_PROPERTIES', categories=None):
            '''======================================
            // List Calendar Events
            //======================================
            /* @param string id 	- item id. takes precendense over timeframe
            * @param string $onbehalf 	- "on behalf" seneder's email
            * @param int $start 	- event start timestamp
            * @param int $end		- event end time
            * 
            * @return object response
            */
            '''
            type = 'CALENDAR'
            return self.listItems(type, id, start, end, on_behalf, shape, categories)

        def synchCalendarEvent(self, on_behalf=None, num_to_synch=10, synch_state=None, shape='DEFAULT_PROPERTIES'):
            '''======================================
            // Synchronize Calendar Events
            //======================================
             * @param string $onbehalf 	    - "on behalf": item owner email
             * @param int num_to_synch      - how many items to synch in one go (max 500)
             * @param string  synch_state   - current synch state, blank on initial synch
             * @param string $shape	    - detail level (enumarted in DefaultShapeNamesType)
             * 
             * @return object response
             */
            '''

            type = 'CALENDAR'

            return self.synchFolder(type, on_behalf, num_to_synch, synch_state, shape)


        def addCalendarEvent(self, subject, body, start, end, attendees, on_behalf=None, \
                             location=None, allday = False, bodyType="TEXT", category="default"):
            '''=====================================
            // Add Calendar Event
            //======================================
            /* @param string $subject  	- event subject 
             * @param int $start 	- event start timestamp
             * @param int $end		- event end time
             * @param array $anttendees	- array of email addresses of invited poeople
             * @param string $body     	- event body
             * @param string $onbehalf 	- "on behalf" seneder's email
             * @param string $location	- event loaction
             * @param bool $allday	- is it an all-day event?
             * @param string $bodyType	- body format (Text/HTML)
             * @param string $category	- event actegory
             * 
             * @return object response
             *
             '''

            createitem = Element('m:CreateItem')
            createitem.set('SendMeetingInvitations', self.types.EWSType_CalendarItemCreateOrDeleteOperationType.SEND_TO_NONE)

            saveditemfolderid = Element('m:SavedItemFolderId')
            distinguishedfolderid = Element('t:DistinguishedFolderId')
            distinguishedfolderid.set('Id', self.types.EWSType_DistinguishedFolderIdNameType.CALENDAR)
            if on_behalf is not None:
                mailbox = Element('t:Mailbox')
                emailaddress = Element('t:EmailAddress').setText(on_behalf)
                mailbox.append(emailaddress)
                distinguishedfolderid.append(mailbox)
            saveditemfolderid.append(distinguishedfolderid)
            createitem.append(saveditemfolderid)

            calitems = Element('m:Items')

            # Prepare objects for CalendarItem creation
            calitem = Element('t:CalendarItem')
            #if we are running MS EX 2010 or newer use different TZ settings
            startTZ = None
            if int(self.exchange.version.majorversion) >= 14:
                startTZ = Element('t:StartTimeZone')
                startTZ.set('Id', self.exchange.TimeZoneId)
                endTZ = Element('t:EndTimeZone')
                endTZ.set('Id', self.exchange.TimeZoneId)
            else:
                timeZone = Element('t:MeetingTimeZone')
                timeZone.set('TimeZoneName', self.exchange.TimeZoneName)
                timeZone.append(Element('t:BaseOffset').setText(self.exchange.BaseOffset))
                standard = Element('t:Standard')
                standard.append(Element('t:Offset').setText(self.exchange.StandardOffset))
                standard.append(Element('t:Time').setText(self.exchange.StandardTime))
                timeZone.append(standard)
                daylight = Element('t:Daylight')
                daylight.append(Element('t:Offset').setText(self.exchange.Offset))
                daylight.append(Element('t:Time').setText(self.exchange.DaylightTime))
                timeZone.append(daylight)

            Subject = Element('t:Subject')
            Body = Element('t:Body')
            Body.set('BodyType', getattr(self.types.EWSType_BodyTypeResponseType, bodyType))
            cats = None
            if category:
                cats = Element('t:Categories')
                if not isinstance(category, list): 
                    cats.append(Element('t:String').setText(category))
                else:
                    for cat in category:
                        cats.append(Element('t:String').setText(cat))
            Start = Element('t:Start')
            End = Element('t:End')
            Location = Element('t:Location')
            alldayevent =  Element('t:IsAllDayEvent')
            calitem.append(Subject.setText(subject))
            calitem.append(Body.setText(body))
            calitem.append(cats)	    
            calitem.append(Start.setText(start.ewsformat()))
            calitem.append(End.setText(end.ewsformat()))	    
            calitem.append(alldayevent.setText(int(allday)))
            if location:
                calitem.append(Location.setText(location))
            atts = Element('t:RequiredAttendees')	    	
            for attendee in attendees:
                att = Element('t:Attendee')	
                mailbox = Element('t:Mailbox')
                emailaddress = Element('t:EmailAddress').setText(attendee)
                mailbox.append(emailaddress)
                att.append(mailbox)
                atts.append(att)
            calitem.append(atts)
            #TZ realted stuff
            if startTZ is not None:
                calitem.append(startTZ)
                calitem.append(endTZ)
            else:
                calitem.append(timeZone)


            #add item to items
            calitems.append(calitem)
            #add item to CreateItems
            createitem.append(calitems)

            #make the call
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
                idlist.extend([item._Id, item._ChangeKey])

            return idlist        

        def editCalendarEvent(self, id, ckey, subject=None, body=None, bodytype="TEXT", \
                              start=None, end=None, location=None, attendees=[], \
                              allday=None, category=None):

            '''======================================
	    // Edit Calendar Event
	    //======================================
	    /* @param string $id  	- event id
	     * @param string $ckey  	- event change key
	     * @param string $subject  	- event subject
	     * @param string $body     	- event body
	     * @param int $start 	- event start timestamp
	     * @param int $end		- event end time
	     * @param string $location 	- event location
	     * @param array $anttendees	- array of email addresses of invited poeople
	     * @param bool $allday	- is it an all-day event?
	     * @param string $category	- event actegory
	     * 
	     * @return object response
	     */
	    '''

            Updates = {
                'calendar:Start' : start.ewsformat() if start else None,
                'calendar:End'	 : end.ewsformat() if end else None,
                'calendar:Location' : location,
                'calendar:IsAllDayEvent' : allday,
                'item:Subject' : subject,
            }

            updateitem = Element('m:UpdateItem')
            updateitem.set('SendMeetingInvitationsOrCancellations', self.types.EWSType_CalendarItemCreateOrDeleteOperationType.SEND_TO_NONE)	    
            updateitem.set('MessageDisposition', self.types.EWSType_MessageDispositionType.SAVEONLY)
            updateitem.set('ConflictResolution', self.types.EWSType_ConflictResolutionType.ALWAYSOVERWRITE)

            itemchanges = Element('m:ItemChanges')
            itemchange = Element('t:ItemChange')
            itemid = Element('t:ItemId')
            itemid.set('Id', id)
            itemid.set('ChangeKey', ckey)
            itemchange.append(itemid)

            updates = Element('t:Updates')

            #popoulate update array
            for key,value in Updates.items():
                if value:
                    prop = key.split(':').pop()
                    itemfield = Element('t:SetItemField')
                    itemfield.append(Element('t:FieldURI'))
                    itemfield.children[0].set('FieldURI', key)
                    itemfield.append(Element('t:CalendarItem'))
                    itemfield.children[1].append(Element('t:'+prop).setText(value))
                    updates.append(itemfield)


            if attendees:
                itemfield = Element('t:SetItemField')
                itemfield.append(Element('t:FieldURI'))
                itemfield.children[0].set('FieldURI', 'calendar:RequiredAttendees')
                itemfield.append(Element('t:CalendarItem'))
                reqatts = Element('t:RequiredAttendees')
                for attendee in attendees:
                    att = Element('t:Attendee')	
                    mailbox = Element('t:Mailbox')
                    emailaddress = Element('t:EmailAddress').setText(attendee)
                    mailbox.append(emailaddress)
                    att.append(mailbox)
                    reqatts.append(att)
                itemfield.children[1].append(reqatts)
                updates.append(itemfield)


            if category:
                itemfield = Element('t:SetItemField')
                itemfield.append(Element('t:FieldURI'))
                itemfield.children[0].set('FieldURI', 'item:Categories')
                itemfield.append(Element('t:CalendarItem'))
                categories = Element('t:Categories')
                if not isinstance(category, list): 
                    categories.append(Element('t:String').setText(category))
                else:
                    for cat in category:
                        categories.append(Element('t:String').setText(cat))               
                itemfield.children[1].append(categories)
                updates.append(itemfield)

            if body:
                itemfield = Element('t:SetItemField')
                itemfield.append(Element('t:FieldURI'))
                itemfield.children[0].set('FieldURI', 'item:Body')
                itemfield.append(Element('t:CalendarItem'))
                Body = Element('t:Body')
                Body.set('BodyType', getattr(self.types.EWSType_BodyTypeResponseType, bodytype))
                Body.setText(body)
                itemfield.children[1].append(Body)
                updates.append(itemfield)

            #timezone
            if int(self.exchange.version.majorversion) >= 14:
                itemfield = Element('t:SetItemField')
                itemfield.append(Element('t:FieldURI'))  
                itemfield.children[0].set('FieldURI', 'calendar:StartTimeZone')
                itemfield.append(Element('t:CalendarItem'))
                startTZ = Element('t:StartTimeZone')
                startTZ.set('Id', self.exchange.TimeZoneId)
                itemfield.children[1].append(startTZ)
                updates.append(itemfield)   
                itemfield = Element('t:SetItemField')
                itemfield.append(Element('t:FieldURI'))  
                itemfield.children[0].set('FieldURI', 'calendar:EndTimeZone')
                itemfield.append(Element('t:CalendarItem'))
                endTZ = Element('t:EndTimeZone')
                endTZ.set('Id', self.exchange.TimeZoneId)
                itemfield.children[1].append(endTZ)
                updates.append(itemfield)                 
            else:
                itemfield = Element('t:SetItemField')
                itemfield.append(Element('t:FieldURI'))  
                itemfield.children[0].set('FieldURI', 'calendar:MeetingTimeZone')                
                timeZone = Element('t:MeetingTimeZone')
                timeZone.set('TimeZoneName', self.exchange.TimeZoneName)
                timeZone.append(Element('t:BaseOffset').setText(self.exchange.BaseOffset))
                standard = Element('t:Standard')
                standard.append(Element('t:Offset').setText(self.exchange.StandardOffset))
                standard.append(Element('t:Time').setText(self.exchange.StandardTime))
                timeZone.append(standard)
                daylight = Element('t:Daylight')
                daylight.append(Element('t:Offset').setText(self.exchange.Offset))
                daylight.append(Element('t:Time').setText(self.exchange.DaylightTime))
                timeZone.append(daylight)            
                itemfield.children[1].append(timeZone)
                updates.append(itemfield)
                
            itemchange.append(updates)
            itemchanges.append(itemchange)
            updateitem.append(itemchanges)

            #make the call
            xml = self.exchange.transport.wrap(updateitem)
            try:
                result = self.client.service.UpdateItem(__inject={'msg':xml})
            except WebFault as e:
                raise e

            # Result may come as a single object or a list of objects
            if type(result.UpdateItemResponseMessage).__name__ == 'list':
                msgs = result.UpdateItemResponseMessage
            else:
                msgs = [result.UpdateItemResponseMessage]

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


        def deleteCalendarEvent(self, ids):
            '''======================================
            // Delete Calendar Event Items
            //======================================
            /* @param array $ids	  	- array of event ids to delete
             * 
             * @return object response
             */	    
            '''
            return self.deleteItems(ids)


        def addTask(self, subject, on_behalf, due, body=None, reminderdue=None, reminderStart="30",\
                    importance="NORMAL", sensitivity="NORMAL", bodyType="TEXT", category="default"):
            '''======================================
            // Add Task
            //======================================
            /* @param string $subject  	- task subject
             * @param string $body     	- task body
             * @param string $onbehalf 	- "on behalf" seneder's email
             * @param int $due 		- task due date timestamp
             * @param int $reminderdue	- reminder due date timestamp
             * @param int $reminderStart	- realtive negative offset for reminder start in nimutes
             * @param string $importance	- task importance
             * @param string $sensitivity	- task sensitivity
             * @param string $bodytype	- task body type (TEXT/HTML)
             * @param string $category	- task category
             * 
             * @return object response
             */
             '''

            createitem = Element('m:CreateItem')

            saveditemfolderid = Element('m:SavedItemFolderId')
            distinguishedfolderid = Element('t:DistinguishedFolderId')
            distinguishedfolderid.set('Id', self.types.EWSType_DistinguishedFolderIdNameType.TASKS)
            if on_behalf is not None:
                mailbox = Element('t:Mailbox')
                emailaddress = Element('t:EmailAddress').setText(on_behalf)
                mailbox.append(emailaddress)
                distinguishedfolderid.append(mailbox)
            saveditemfolderid.append(distinguishedfolderid)
            createitem.append(saveditemfolderid)

            tasks = Element('m:Items')

            # Prepare objects for Task creation
            task = Element('t:Task')
            Subject = Element('t:Subject')
            Sensitivity = Element('t:Sensitivity')
            cats = None
            if category:
                cats = Element('t:Categories')
                cats.append(Element('t:String').setText(category))
            Importance = Element('t:Importance')
            ReminderDueBy = Element('t:ReminderDueBy')
            ReminderMinutesBeforeStart = Element('t:ReminderMinutesBeforeStart')
            ReminderIsSet =  Element('t:ReminderIsSet')
            DueDate = Element('t:DueDate')
            task.append(Subject.setText(subject))
            task.append(Sensitivity.setText(getattr(self.types.EWSType_SensitivityChoicesType, sensitivity)))
            if body:
                Body = Element('t:Body')
                Body.set('BodyType', getattr(self.types.EWSType_BodyTypeResponseType, bodyType))
                task.append(Body.setText(body))	
            task.append(cats)
            task.append(Importance.setText(getattr(self.types.EWSType_ImportanceChoicesType,importance)))	    
            if(reminderdue):
                task.append(ReminderDueBy.setText(reminderdue.ewsformat()))
                task.append(ReminderIsSet.setText(1))		
                task.append(ReminderMinutesBeforeStart.setText(reminderStart))	    
            task.append(DueDate.setText(due.ewsformat()))


            #add item to items
            tasks.append(task)
            #add item to CreateItems
            createitem.append(tasks)

            #make the call
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

                item = msg.Items.Task.ItemId
                idlist.append((item._Id, item._ChangeKey))

            return idlist     	


        def editTask(self, id, ckey, subject=None, body=None, bodytype='TEXT', due=None, \
                     reminderdue=None, reminderStart=None, status=None, percentComplete=None, \
                     sensitivity=None, importance=None, category=None):	    
            '''======================================
            // Edit Task
            //======================================
            /* @param string $id  	   - event id
             * @param string $ckey  	   - event change key
             * @param string $subject  	   - event subject
             * @param string $body     	   - task body
             * @param string $bodytype	   - task body type (TEXT/HTML) 
             * @param int $due 		   - task due date timestamp
             * @param int $reminderdue	   - reminder due date timestamp
             * @param int $reminderStart   - realtive negative offset for reminder start in nimutes
             * @param string $status	   - task status (enumarted in TaskStatusType)
             * @param int $percentComplete - task complitionprocentage
             * @param string $sensitivity  - task sensitivity (enumarted in SensitivityChoicesType)
             * @param string $importance   - task importance (enumarted in ImportanceChoicesType)
             * @param string $category	   - task category
             * 
             * @return object response
             */
            '''

            Updates = {
                'task:DueDate'                    : due.ewsformat() if due else None,
                'item:ReminderDueBy'	          : reminderdue.ewsformat() if reminderdue else None,
                'item:ReminderMinutesBeforeStart' : reminderStart,
                'item:ReminderIsSet'              : 1 if (reminderStart or reminderdue) else 0,
                'item:Subject'                    : subject,	        
                'task:Status'                     : getattr(self.types.EWSType_TaskStatusType, status) if status else None,
                'item:Sensitivity'                : getattr(self.types.EWSType_SensitivityChoicesType, sensitivity) if sensitivity else None,
                'item:Importance'                 : getattr(self.types.EWSType_ImportanceChoicesType, importance) if importance else None,
                'task:PercentComplete'            : percentComplete
            }

            updateitem = Element('m:UpdateItem')
            updateitem.set('SendMeetingInvitationsOrCancellations', self.types.EWSType_CalendarItemCreateOrDeleteOperationType.SEND_TO_ALL_AND_SAVE_COPY)	    
            updateitem.set('MessageDisposition', self.types.EWSType_MessageDispositionType.SAVEONLY)
            updateitem.set('ConflictResolution', self.types.EWSType_ConflictResolutionType.ALWAYSOVERWRITE)

            itemchanges = Element('m:ItemChanges')
            itemchange = Element('t:ItemChange')
            itemid = Element('t:ItemId')
            itemid.set('Id', id)
            itemid.set('ChangeKey', ckey)
            itemchange.append(itemid)

            updates = Element('t:Updates')

            #popoulate update array
            for key,value in Updates.items():
                if value:
                    prop = key.split(':').pop()
                    itemfield = Element('t:SetItemField')
                    itemfield.append(Element('t:FieldURI'))
                    itemfield.children[0].set('FieldURI', key)
                    itemfield.append(Element('t:Task'))
                    itemfield.children[1].append(Element('t:'+prop).setText(value))
                    updates.append(itemfield)

            if category:
                itemfield = Element('t:SetItemField')
                itemfield.append(Element('t:FieldURI'))
                itemfield.children[0].set('FieldURI', 'item:Categories')
                itemfield.append(Element('t:Task'))
                categories = Element('t:Categories')
                categories.append(Element('t:String').setText(category))		
                itemfield.children[1].append(categories)
                updates.append(itemfield)

            if body:
                itemfield = Element('t:SetItemField')
                itemfield.append(Element('t:FieldURI'))
                itemfield.children[0].set('FieldURI', 'item:Body')
                itemfield.append(Element('t:Task'))
                Body = Element('t:Body')
                Body.set('BodyType', getattr(self.types.EWSType_BodyTypeResponseType, bodytype))
                Body.setText(body)
                itemfield.children[1].append(Body)
                updates.append(itemfield)

            itemchange.append(updates)
            itemchanges.append(itemchange)
            updateitem.append(itemchanges)

            #make the call
            xml = self.exchange.transport.wrap(updateitem)
            try:
                result = self.client.service.UpdateItem(__inject={'msg':xml})
            except WebFault as e:
                raise e

            # Result may come as a single object or a list of objects
            if type(result.UpdateItemResponseMessage).__name__ == 'list':
                msgs = result.UpdateItemResponseMessage
            else:
                msgs = [result.UpdateItemResponseMessage]

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

                item = msg.Items.Task.ItemId
                idlist.append((item._Id, item._ChangeKey))

            return idlist  


        def deleteTask(self, ids):
            '''======================================
            // Delete Task Items
            //======================================
            /* @param array $ids	  	- array of taks ids to delete
             * 
             * @return object response
             */	    
            '''
            return self.deleteItems(ids)


        def listTask(self, id=None, start=None, end=None, on_behalf=None, shape='DEFAULT_PROPERTIES', categories=None):
            '''======================================
            // List Calendar Events
            //======================================
            /* @param string id 	- item id. takes precendense over timeframe
            * @param string $onbehalf 	- "on behalf" seneder's email
            * @param int $start 	- event start timestamp
            * @param int $end		- event end time
            * 
            * @return object response
            */
            '''
            type = 'TASKS'
            return self.listItems(type, id, start, end, on_behalf, shape, categories)


        def deleteItems(self, ids):
            '''======================================
            // Delete Items
            //======================================
            /* @param array $ids - list of item ids to delete
             * 
             * @return list of tuples (success[True|False], errormessage)
             * 
             '''

            status = []
            if not ids:
                # Nothing to do
                return status

            deleteitem = Element('m:DeleteItem')
            deleteitem.set('DeleteType', self.types.EWSType_DisposalType.MOVE_TO_DELETED_ITEMS)
            deleteitem.set('SendMeetingCancellations', self.types.EWSType_CalendarItemCreateOrDeleteOperationType.SEND_TO_NONE)
            deleteitem.set('AffectedTaskOccurrences', self.types.EWSType_AffectedTaskOccurrencesType.ALL_OCCURRENCES)

            itemids = Element('m:ItemIds')
            itemid = Element('t:ItemId')

            # copy.deepcopy() is faster than having Element() inside the loop. 
            for iid in ids:
                i = deepcopy(itemid)
                i.set('Id', iid)
                #i.set('ChangeKey', changekey)
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

        def listItems(self, type, id=None, start=None, end=None, on_behalf=None, shape='ID_ONLY', categories=[], additional=[]):
            '''======================================
            // List Items
            // Note: currenttly only Taska are 
            // searcheble by category
            //======================================
            /* @param string type	- item type
            * @param string id 	- item id. takes precendense over timeframe
            * @param string $onbehalf 	- "on behalf": item owner email
            * @param int $start 	- search start timestamp
            * @param int $end		- search end timestamp
            * 
            * @return object response
            */
            '''

            if(id):
                getitem = Element('m:GetItem')
                itemshape = Element('m:ItemShape')
                baseshape = Element('t:BaseShape').setText(getattr(self.types.EWSType_DefaultShapeNamesType, shape))
                itemshape.append(baseshape)

                if additional:
                    additionalproperties = Element('t:AdditionalProperties')
                    for URI in additional:
                        fielduri = Element('t:FieldURI')
                        fielduri.set('FieldURI', URI)
                        additionalproperties.append(fielduri)

                    itemshape.append(additionalproperties)

                getitem.append(itemshape)

                itemids = Element('m:ItemIds')
                if isinstance(id, list):
                    for single in id:
                        itemid = Element('t:ItemId')
                        itemid.set('Id', single)
                        itemids.append(itemid)			

                else:
                    itemid = Element('t:ItemId')
                    itemid.set('Id', id)
                    itemids.append(itemid)
                getitem.append(itemids)
                xml = self.exchange.transport.wrap(getitem)

                try:
                    result = self.client.service.GetItem(__inject={'msg':xml})
                except WebFault as e:
                    raise e
                msg = result.GetItemResponseMessage
                if isinstance(msg, list):
                    fullitems = []
                    for el in msg:
                        rspclass = el._ResponseClass
                        rspcode = el.ResponseCode
                        if rspclass == 'Error':
                            raise Exception('Error code: %s message: %s' % \
                                            (rspcode, msg.MessageText))
                        if rspclass != 'Success':
                            raise Exception('Unknown response class: %s code: %s' % \
                                            (rspclass, rspcode))

                        if rspcode != 'NoError':
                            raise Exception('Unknown response code: %s' % rspcode)

                        fullitems.extend([el.Items[0]])

                    #print fullitems
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
                else:
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

                    if isinstance(msg.Items[0], list):
                        fullitems = msg.RootFolder.Items[0]
                    else:
                        # Only one item returned
                        fullitems = [msg.Items].pop()

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

            else:
                finditem = Element('m:FindItem')
                finditem.set('Traversal', self.types.EWSType_FolderQueryTraversalType.SHALLOW)

                itemshape = Element('m:ItemShape')
                baseshape = Element('t:BaseShape').setText(getattr(self.types.EWSType_DefaultShapeNamesType, shape))
                itemshape.append(baseshape)
                additionalproperties = None

                # additional properties
                if categories:
                    additionalproperties = Element('t:AdditionalProperties')
                    fielduri = Element('t:FieldURI')
                    fielduri.set('FieldURI', 'item:Categories')
                    additionalproperties.append(fielduri)

                #append all additional properties, if any
                if additionalproperties:
                    itemshape.append(additionalproperties)
                finditem.append(itemshape)

                #type-sepcific options
                if(type == 'CALENDAR'):
                    if start or end:
                        calendarview = Element('m:CalendarView')
                        if start:    
                            calendarview.set('StartDate', start.ewsformat())
                        if end:   
                            calendarview.set('EndDate', end.ewsformat())
                        finditem.append(calendarview)

                elif(type == 'TASKS'):
                    if start or end:
                        res = Element('m:Restriction')
                        restriction = Element('t:And')
                    if not start:
                        start = EWSDateTime(0)
                    if not end:
                        end = EWSDateTime(2038, 1, 1, 0, 0, 0)
                    rcount = len([f for f in [start, end, categories] if f != None])
                    if categories:
                        if not res:
                            restriction = Element('m:Restriction')
                        if len(categories) == 1:
                            restriction.append(self._restriction('contains', 'item:Categories', categories[0]))
                        else:
                            ortype = Element('t:Or')
                            for cat in categories:
                                ortype.append(self._restriction('contains', 'item:Categories', cat))
                            restriction.append(ortype)
                    extended = self._mapi_reference('33029', 'SystemTime', 'Task')
                    gteq = self._restriction('>=', extended, start.ewsformat(), True)
                    restriction.append(gteq)
                    lseq = self._restriction('<=', extended, end.ewsformat(), True)
                    restriction.append(lseq)

                    if rcount > 1:
                        res.append(restriction)
                        finditem.append(res)	
                    else:
                        finditem.append(restriction)

                distinguishedfolderid = Element('t:DistinguishedFolderId')
                distinguishedfolderid.set('Id', getattr(self.types.EWSType_DistinguishedFolderIdNameType, type))
                parentfolderids = Element('m:ParentFolderIds')
                mailbox = Element('t:Mailbox')
                emailaddress = Element('t:EmailAddress').setText(on_behalf)
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

                if isinstance(msg.RootFolder.Items[0], list):
                    fullitems = msg.RootFolder.Items[0]
                else:
                    # Only one item returned
                    fullitems = msg.RootFolder.Items

                #if we have addtional proerties to fetch do so

                #get ids from response
                ids = self.getids(fullitems, False)
                #call self with ids and required props
                if type=="CALENDAR":
                    additional.append("calendar:RequiredAttendees")
                    additional.append("calendar:IsAllDayEvent")
                    additional.append("calendar:Duration")
                    additional.append("item:Categories")
                    additional.append("item:Body")
                    additional.append("item:Sensitivity")
                    additional.append("item:Importance")
                    extended_items = self.listItems(type="CALENDAR", id=ids, additional=additional)
                    #print extended_items
                    #print ids
                    #exit()
                    extended_add, extended_fday, extended_cats, extended_body = ({} for i in range(4))
                    extended_sen, extended_imp = ({} for i in range(2))
                    for i in range(0, len(extended_items)):
                        if hasattr(extended_items[i], 'RequiredAttendees'):
                            extended_add[extended_items[i].ItemId._Id] = extended_items[i].RequiredAttendees
                        else:
                            extended_add[extended_items[i].ItemId._Id] = []
                        extended_fday[extended_items[i].ItemId._Id] = extended_items[i].IsAllDayEvent
                        extended_cats[extended_items[i].ItemId._Id] = extended_items[i].Categories if hasattr(extended_items[i], "Categories") else None
                        extended_body[extended_items[i].ItemId._Id] = extended_items[i].Body if hasattr(extended_items[i], "Body") else None
                        extended_sen[extended_items[i].ItemId._Id] = extended_items[i].Sensitivity
                        extended_imp[extended_items[i].ItemId._Id] = extended_items[i].Importance
                    for i in range(0,len(fullitems)):
                        fullitems[i].RequiredAttendees = extended_add.get(fullitems[i].ItemId._Id)
                        fullitems[i].IsAllDayEvent = extended_fday.get(fullitems[i].ItemId._Id)
                        fullitems[i].Categories = extended_cats.get(fullitems[i].ItemId._Id)
                        fullitems[i].Body = extended_body.get(fullitems[i].ItemId._Id)
                        fullitems[i].Sensitivity = extended_sen.get(fullitems[i].ItemId._Id)
                        fullitems[i].Importance = extended_imp.get(fullitems[i].ItemId._Id)

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

        def listFolders(self, type, on_behalf, shape='DEFAULT_PROPERTIES', depth='SHALLOW'):
            '''======================================
            // List Folders
            //======================================
            /* @param string type	- folder type (enumarted in DistinguishedFolderIdNameType)
             * @param string $onbehalf 	- "on behalf": item owner email
             * @param string $shape	- detail level (enumarted in DefaultShapeNamesType)
             * @param string $depth	- list normal /include subfolders (enumarted in FolderQueryTraversalType)	     
             * 
             * @return object response
             */
            '''

            # start building the find folder request
            request =  Element('m:FindFolder')
            request.set('Traversal', getattr(self.types.EWSType_FolderQueryTraversalType, depth))

            itemshape = Element('m:FolderShape')
            baseshape = Element('t:BaseShape').setText(getattr(self.types.EWSType_DefaultShapeNamesType,shape))
            itemshape.append(baseshape)
            request.append(itemshape)

            # configure the view
            indexedpage = Element('m:IndexedPageFolderView')
            indexedpage.set('BasePoint', 'Beginning')
            indexedpage.set('Offset', '0')
            request.append(indexedpage)

            # set the starting folder as the inbox

            distinguishedfolderid = Element('t:DistinguishedFolderId')
            distinguishedfolderid.set('Id', getattr(self.types.EWSType_DistinguishedFolderIdNameType, type))
            parentfolderids = Element('m:ParentFolderIds')
            mailbox = Element('t:Mailbox')
            emailaddress = Element('t:EmailAddress').setText(on_behalf)
            mailbox.append(emailaddress)
            distinguishedfolderid.append(mailbox)
            parentfolderids.append(distinguishedfolderid)
            request.append(parentfolderids)

            xml = self.exchange.transport.wrap(request)

            try:
                result = self.client.service.FindFolder(__inject={'msg':xml})
            except WebFault as e:
                raise e
            msg = result.FindFolderResponseMessage

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

            if isinstance(msg.RootFolder.Folders[0], list):
                fullitems = msg.RootFolder.Folders[0]
            else:
                # Only one item returned
                fullitems = [msg.RootFolder.Folders].pop()

            return fullitems



        def getids(self, items, include_change_key=True):
            '''Takes a list of items with full or partial properties as
            produced from getitems() and returns a list of (id, changekey)
            tuples.'''
            idlist = []
            if len(items) > 1:
                try:
                    for item in [i.ItemId for i in items]:
                        if(include_change_key):
                            idlist.append((item._Id, item._ChangeKey))
                        else:
                            idlist.append(item._Id)
                except AttributeError:
                    for item in [i.ItemId for i in [j[0] for j in items]]:
                        if(include_change_key):
                            idlist.append((item._Id, item._ChangeKey))
                        else:
                            idlist.append(item._Id)                    
            else:
                try:
                    for item in [i.ItemId for i in [j[1] for j in items]]:
                        if(include_change_key):
                            idlist.append((item._Id, item._ChangeKey))
                        else:
                            idlist.append(item._Id)
                except (IndexError,AttributeError):
                    for item in [j.ItemId for j in items]:
                        if(include_change_key):
                            idlist.append((item._Id, item._ChangeKey))
                        else:
                            idlist.append(item._Id)                        
            return idlist
        
        def synchFolder(self, type, on_behalf=None, num_to_synch=10, synch_state=None, shape='ID_ONLY', additional=[], ignored_items=None):
            '''======================================
            // Synch Folder - synchronizes given folder
            //======================================
            /* @param string type	    - folder type (enumarted in DistinguishedFolderIdNameType)
             * @param string $onbehalf 	    - "on behalf": item owner email
             * @param int num_to_synch      - how many items to synch in one go (max 500)
             * @param string  synch_state   - current synch state, blank on initial synch
             * @param string $shape	    - detail level (enumarted in DefaultShapeNamesType)
             * @param string $ignored_items - list of IDs of ignored items (currently not implemented)     
             * 
             * @return object response
             */
            '''
            synchfolder = Element('m:SyncFolderItems')

            itemshape = Element('m:ItemShape')
            baseshape = Element('t:BaseShape').setText(getattr(self.types.EWSType_DefaultShapeNamesType, shape))
            itemshape.append(baseshape)
            synchfolder.append(itemshape)
            
            distinguishedfolderid = Element('t:DistinguishedFolderId')
            distinguishedfolderid.set('Id', getattr(self.types.EWSType_DistinguishedFolderIdNameType, type))
            parentfolderids = Element('m:SyncFolderId')
            mailbox = Element('t:Mailbox')
            emailaddress = Element('t:EmailAddress').setText(on_behalf)
            mailbox.append(emailaddress)
            distinguishedfolderid.append(mailbox)
            parentfolderids.append(distinguishedfolderid)
            synchfolder.append(parentfolderids)
            
            if synch_state is not None:
                synchstate = Element('m:SyncState').setText(synch_state)
                synchfolder.append(synchstate)

            if ignored_items:
                #@TODO : add ignored items...
                pass
            
            numresults = Element('m:MaxChangesReturned').setText(num_to_synch)
            synchfolder.append(numresults)
            
            xml = self.exchange.transport.wrap(synchfolder)
            
            try:
                result = self.client.service.SyncFolderItems(__inject={'msg':xml})
            except WebFault as e:
                raise e
            msg = result.SyncFolderItemsResponseMessage

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
            if not msg.IncludesLastItemInRange:
                self.hasMoreItems = True
            else:
                self.hasMoreItems = False
            if msg.SyncState:
                self.synchState = msg.SyncState

            #if isinstance(msg.Changes[0], list):
            #    fullitems = msg.Changes[0]
            #else:
                # Only one item returned
            changes          = msg.Changes
            fullitems        = []
            __fullitems      = []
            ids              = []
            fullitems_add    = []
            fullitems_update = []
            
            #add/update events
            if hasattr(changes, 'Create'):
                if isinstance(changes.Create[0], list):
                    __fullitems.extend(changes.Create[0])
                else:
                    __fullitems.extend(changes.Create)
                #fix attributes
                if len(__fullitems) > 1:
                    for elem in __fullitems:
                        fullitems.append(elem[0])
                else:
                    for elem in __fullitems:
                        fullitems.append(elem[1])  
                #get ids from response
                ids.extend(self.getids(fullitems, False))
                fullitems_add = fullitems
                fullitems = []
                __fullitems = []
            
            if hasattr(changes, 'Update'):
                if isinstance(changes.Update[0], list):
                    __fullitems.extend(changes.Update[0])
                else:
                    __fullitems.extend(changes.Update)                
                 #fix attributes
                if len(__fullitems) > 1:
                    for elem in __fullitems:
                        fullitems.append(elem[0])
                else:
                    for elem in __fullitems:
                        fullitems.append(elem[1])  
                #get ids from response
                ids.extend(self.getids(fullitems, False))
                fullitems_update = fullitems
                fullitems = []
                __fullitems = []
                
            #if we have addtional proerties to fetch do so

            #join fulltimes toghether
            fullitems = fullitems_add + fullitems_update
                                        
            
            #call self with ids and required props
            if type=="CALENDAR":
                if ids:
                    additional.append("calendar:RequiredAttendees")
                    additional.append("calendar:IsAllDayEvent")
                    additional.append("calendar:Duration")
                    additional.append("item:Categories")
                    additional.append("item:Body")
                    additional.append("item:Sensitivity")
                    additional.append("item:Importance")
                    extended_items = self.listItems(type="CALENDAR", id=ids, additional=additional)
                    #print extended_items
                    #print ids
                    #exit()
                    extended_add, extended_fday, extended_cats, extended_body = ({} for i in range(4))
                    extended_sen, extended_imp = ({} for i in range(2))
                    for i in range(0, len(extended_items)):
                        if hasattr(extended_items[i], 'RequiredAttendees'):
                            extended_add[extended_items[i].ItemId._Id] = extended_items[i].RequiredAttendees
                        else:
                            extended_add[extended_items[i].ItemId._Id] = []
                        extended_fday[extended_items[i].ItemId._Id] = extended_items[i].IsAllDayEvent
                        extended_cats[extended_items[i].ItemId._Id] = extended_items[i].Categories if hasattr(extended_items[i], "Categories") else None
                        extended_body[extended_items[i].ItemId._Id] = extended_items[i].Body if hasattr(extended_items[i], "Body") else None
                        extended_sen[extended_items[i].ItemId._Id] = extended_items[i].Sensitivity
                        extended_imp[extended_items[i].ItemId._Id] = extended_items[i].Importance
                    try:
                        for i in range(0,len(fullitems)):
                            fullitems[i].RequiredAttendees = extended_add.get(fullitems[i].ItemId._Id)
                            fullitems[i].IsAllDayEvent = extended_fday.get(fullitems[i].ItemId._Id)
                            fullitems[i].Categories = extended_cats.get(fullitems[i].ItemId._Id)
                            fullitems[i].Body = extended_body.get(fullitems[i].ItemId._Id)
                            fullitems[i].Sensitivity = extended_sen.get(fullitems[i].ItemId._Id)
                            fullitems[i].Importance = extended_imp.get(fullitems[i].ItemId._Id)
                    except AttributeError:
                        fullitems.RequiredAttendees = extended_add.get(fullitems.ItemId._Id)
                        fullitems.IsAllDayEvent = extended_fday.get(fullitems.ItemId._Id)
                        fullitems.Categories = extended_cats.get(fullitems.ItemId._Id)
                        fullitems.Body = extended_body.get(fullitems.ItemId._Id)
                        fullitems.Sensitivity = extended_sen.get(fullitems.ItemId._Id)
                        fullitems.Importance = extended_imp.get(fullitems.ItemId._Id)
                    if(len(fullitems) < 2):
                        fullitems =  [("EventSpoofedType",fullitems.pop())]
            
            #allitems = type('', (object,), {})
            allitems = lambda:0
            allitems.addupdate = fullitems
            if hasattr(changes, 'Delete'):
                if len(changes.Delete) < 2:
                    allitems.delete = [changes.Delete]
                else:    
                    allitems.delete = changes.Delete
            return allitems            


class EWSDateTime(datetime):
    '''Extends the normal datetime implementation to satisfy Exchange'''

    def ewsformat(self):
        '''ISO 8601 format to satisfy xs:datetime as interpreted by Exchange'''
        return self.strftime('%Y-%m-%dT%H:%M:%S')

    def midnightfix(self):
        return self - timedelta(seconds=1)

    def __new__(cls, y=None, m=None, d=None, h=None, mi=None, s=None):
        if((y>=0) and (all(x is None for x in (m,d,h,mi,s)))): 
            t = datetime.fromtimestamp(y)
            return super(EWSDateTime, cls).__new__(cls,t.year,t.month,t.day,t.hour,t.minute,t.second)
        else:
            return super(EWSDateTime, cls).__new__(cls,y,m,d,h,mi,s)
