##
# Definition of the DelegateUserType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the DelegateUserType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_DelegateUserType (EWSType):
	##
	# UserId property
	#
	# @var EWSType_UserIdType
	#
	self.UserId=''
	##
	# DelegatePermissions property
	#
	# @var EWSType_DelegatePermissionsType
	#
	self.DelegatePermissions=''
	##
	# ReceiveCopiesOfMeetingMessages property
	#
	# @var EWSType_boolean
	#
	self.ReceiveCopiesOfMeetingMessages=''
	##
	# ViewPrivateItems property
	#
	# @var EWSType_boolean
	#
	self.ViewPrivateItems=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'UserId',
		'required' : False,
		'type' : 'UserIdType',
		},
		{'name' : 'DelegatePermissions',
		'required' : False,
		'type' : 'DelegatePermissionsType',
		},
		{'name' : 'ReceiveCopiesOfMeetingMessages',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'ViewPrivateItems',
		'required' : False,
		'type' : 'boolean',
		},
		]
# end this->schema
# end function __construct()
# end class DelegateUserType
