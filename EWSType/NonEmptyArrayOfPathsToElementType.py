##
# Definition of the NonEmptyArrayOfPathsToElementType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the NonEmptyArrayOfPathsToElementType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_NonEmptyArrayOfPathsToElementType (EWSType):
	##
	# Path property
	#
	# @var EWSType_BasePathToElementType
	#
	self.Path=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'Path',
		'required' : False,
		'type' : 'BasePathToElementType',
		},
		]
# end this->schema
# end function __construct()
# end class NonEmptyArrayOfPathsToElementType
