##
# Definition of the BaseResponseMessageType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the BaseResponseMessageType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_BaseResponseMessageType (EWSType):
	##
	# ResponseMessages property
	#
	# @var EWSType_ArrayOfResponseMessagesType
	#
	self.ResponseMessages=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'ResponseMessages',
		'required' : False,
		'type' : 'ArrayOfResponseMessagesType',
		},
		]
# end this->schema
# end function __construct()
# end class BaseResponseMessageType
