##
# Definition of the GetUserAvailabilityRequestType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the GetUserAvailabilityRequestType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_GetUserAvailabilityRequestType (EWSType):
	##
	# TimeZone property
	#
	# @var EWSType_SerializableTimeZone
	#
	self.TimeZone=''
	##
	# MailboxDataArray property
	#
	# @var EWSType_ArrayOfMailboxData
	#
	self.MailboxDataArray=''
	##
	# FreeBusyViewOptions property
	#
	# @var EWSType_FreeBusyViewOptionsType
	#
	self.FreeBusyViewOptions=''
	##
	# SuggestionsViewOptions property
	#
	# @var EWSType_SuggestionsViewOptionsType
	#
	self.SuggestionsViewOptions=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'TimeZone',
		'required' : False,
		'type' : 'SerializableTimeZone',
		},
		{'name' : 'MailboxDataArray',
		'required' : False,
		'type' : 'ArrayOfMailboxData',
		},
		{'name' : 'FreeBusyViewOptions',
		'required' : False,
		'type' : 'FreeBusyViewOptionsType',
		},
		{'name' : 'SuggestionsViewOptions',
		'required' : False,
		'type' : 'SuggestionsViewOptionsType',
		},
		]
# end this->schema
# end function __construct()
# end class GetUserAvailabilityRequestType
