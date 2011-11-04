#get basepath
import os
BASE_PATH = ''
BASE_PATH = os.path.normpath(os.path.dirname( os.path.realpath( __file__ )))
BASE_PATH = BASE_PATH.replace('\\', '/')

#setup suds debbuging messages
import logging
logging.getLogger('suds.client').setLevel(logging.DEBUG)
logging.getLogger('suds.transport').setLevel(logging.DEBUG)
logging.getLogger('suds.xsd.schema').setLevel(logging.DEBUG)
logging.getLogger('suds.wsdl').setLevel(logging.DEBUG)

#setup client
import suds 
from suds.client import Client 
from suds.transport.https import WindowsHttpAuthenticated

url = 'file:///' + BASE_PATH + '/wsdl/services.wsdl'
user = 'crm@dknotus.pl'
passwd = 'Haslo55!'

ntlm = WindowsHttpAuthenticated(username=user,password=password) 
client = Client(url, transport=ntlm)


'''
from suds.client import Client
#from suds.transport.https import WindowsHttpAuthenticated
#ntlm = WindowsHttpAuthenticated(username=userid, password=passwd)
#client = Client(url, transport=ntlm)
client = Client(url)
#url = 'https://red002.mail.emea.microsoftonline.com/EWS/Exchange.asmx'
import urllib2
baseurl = 'https://red002.mail.emea.microsoftonline.com/EWS/Exchange.asmx'
username = 'crm@dknotus.pl'
password = 'Haslo55!'
passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
passman.add_password(None, baseurl, username, password)
authhandler = urllib2.HTTPBasicAuthHandler(passman)

client.options.transport.urlopener  = urllib2.build_opener(authhandler)
'''