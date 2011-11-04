##
# Definition of the GetDelegateType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the GetDelegateType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_GetDelegateType (EWSType):
	##
	# UserIds property
	#
	# @var EWSType_ArrayOfUserIdType
	#
	self.UserIds=''
	##
	# IncludePermissions property
	#
	# @var EWSType_boolean
	#
	self.IncludePermissions=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'UserIds',
		'required' : False,
		'type' : 'ArrayOfUserIdType',
		},
		{'name' : 'IncludePermissions',
		'required' : False,
		'type' : 'boolean',
		},
		]
# end this->schema
# end function __construct()
# end class GetDelegateType
