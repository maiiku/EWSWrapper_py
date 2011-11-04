##
# Definition of the ArrayOfUserIdType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the ArrayOfUserIdType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_ArrayOfUserIdType (EWSType):
	##
	# UserId property
	#
	# @var EWSType_UserIdType
	#
	self.UserId=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'UserId',
		'required' : False,
		'type' : 'UserIdType',
		},
		]
# end this->schema
# end function __construct()
# end class ArrayOfUserIdType
