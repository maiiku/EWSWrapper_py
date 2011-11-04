##
# Definition of the ResolveNamesResponseMessageType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the ResolveNamesResponseMessageType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_ResolveNamesResponseMessageType (EWSType):
	##
	# ResolutionSet property
	#
	# @var EWSType_ArrayOfResolutionType
	#
	self.ResolutionSet=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'ResolutionSet',
		'required' : False,
		'type' : 'ArrayOfResolutionType',
		},
		]
# end this->schema
# end function __construct()
# end class ResolveNamesResponseMessageType
