##
# Definition of the FolderInfoResponseMessageType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the FolderInfoResponseMessageType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_FolderInfoResponseMessageType (EWSType):
	##
	# Folders property
	#
	# @var EWSType_ArrayOfFoldersType
	#
	self.Folders=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'Folders',
		'required' : False,
		'type' : 'ArrayOfFoldersType',
		},
		]
# end this->schema
# end function __construct()
# end class FolderInfoResponseMessageType
