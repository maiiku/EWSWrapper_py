##
# Definition of the BaseDelegateResponseMessageType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the BaseDelegateResponseMessageType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_BaseDelegateResponseMessageType (EWSType):
	##
	# ResponseMessages property
	#
	# @var EWSType_ArrayOfDelegateUserResponseMessageType
	#
	self.ResponseMessages=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'ResponseMessages',
		'required' : False,
		'type' : 'ArrayOfDelegateUserResponseMessageType',
		},
		]
# end this->schema
# end function __construct()
# end class BaseDelegateResponseMessageType
