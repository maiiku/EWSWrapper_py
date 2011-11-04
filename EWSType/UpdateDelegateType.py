##
# Definition of the UpdateDelegateType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the UpdateDelegateType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_UpdateDelegateType (EWSType):
	##
	# DelegateUsers property
	#
	# @var EWSType_ArrayOfDelegateUserType
	#
	self.DelegateUsers=''
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
		self.schema = [{'name' : 'DelegateUsers',
		'required' : False,
		'type' : 'ArrayOfDelegateUserType',
		},
		{'name' : 'DeliverMeetingRequests',
		'required' : False,
		'type' : 'DeliverMeetingRequestsType',
		},
		]
# end this->schema
# end function __construct()
# end class UpdateDelegateType
