##
# Definition of the FindFolderResponseMessageType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the FindFolderResponseMessageType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_FindFolderResponseMessageType (EWSType):
	##
	# RootFolder property
	#
	# @var EWSType_FindFolderParentType
	#
	self.RootFolder=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'RootFolder',
		'required' : False,
		'type' : 'FindFolderParentType',
		},
		]
# end this->schema
# end function __construct()
# end class FindFolderResponseMessageType
