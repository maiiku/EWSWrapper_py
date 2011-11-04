##
# Definition of the GetUserAvailabilityResponseType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the GetUserAvailabilityResponseType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_GetUserAvailabilityResponseType (EWSType):
	##
	# FreeBusyResponseArray property
	#
	# @var EWSType_ArrayOfFreeBusyResponse
	#
	self.FreeBusyResponseArray=''
	##
	# SuggestionsResponse property
	#
	# @var EWSType_SuggestionsResponseType
	#
	self.SuggestionsResponse=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'FreeBusyResponseArray',
		'required' : False,
		'type' : 'ArrayOfFreeBusyResponse',
		},
		{'name' : 'SuggestionsResponse',
		'required' : False,
		'type' : 'SuggestionsResponseType',
		},
		]
# end this->schema
# end function __construct()
# end class GetUserAvailabilityResponseType
