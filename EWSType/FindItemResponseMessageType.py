##
# Definition of the FindItemResponseMessageType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the FindItemResponseMessageType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_FindItemResponseMessageType (EWSType):
	##
	# RootFolder property
	#
	# @var EWSType_FindItemParentType
	#
	self.RootFolder=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'RootFolder',
		'required' : False,
		'type' : 'FindItemParentType',
		},
		]
# end this->schema
# end function __construct()
# end class FindItemResponseMessageType
