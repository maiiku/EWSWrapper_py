##
# Definition of the RemoveDelegateType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the RemoveDelegateType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_RemoveDelegateType (EWSType):
	##
	# UserIds property
	#
	# @var EWSType_ArrayOfUserIdType
	#
	self.UserIds=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'UserIds',
		'required' : False,
		'type' : 'ArrayOfUserIdType',
		},
		]
# end this->schema
# end function __construct()
# end class RemoveDelegateType
