##
# Definition of the ArrayOfDelegateUserType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the ArrayOfDelegateUserType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_ArrayOfDelegateUserType (EWSType):
	##
	# DelegateUser property
	#
	# @var EWSType_DelegateUserType
	#
	self.DelegateUser=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'DelegateUser',
		'required' : False,
		'type' : 'DelegateUserType',
		},
		]
# end this->schema
# end function __construct()
# end class ArrayOfDelegateUserType
