##
# Definition of the GetDelegateResponseMessageType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the GetDelegateResponseMessageType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_GetDelegateResponseMessageType (EWSType):
	##
	# DeliverMeetingRequests property
	#
	# @var EWSType_DeliverMeetingRequestsType
	#
	self.DeliverMeetingRequests=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'DeliverMeetingRequests',
		'required' : False,
		'type' : 'DeliverMeetingRequestsType',
		},
		]
# end this->schema
# end function __construct()
# end class GetDelegateResponseMessageType
