##
# Definition of the ArrayOfFreeBusyResponse type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the ArrayOfFreeBusyResponse type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_ArrayOfFreeBusyResponse (EWSType):
	##
	# FreeBusyResponse property
	#
	# @var EWSType_FreeBusyResponseType
	#
	self.FreeBusyResponse=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'FreeBusyResponse',
		'required' : False,
		'type' : 'FreeBusyResponseType',
		},
		]
# end this->schema
# end function __construct()
# end class ArrayOfFreeBusyResponse
