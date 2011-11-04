##
# Definition of the GetFolderType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the GetFolderType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_GetFolderType (EWSType):
	##
	# FolderShape property
	#
	# @var EWSType_FolderResponseShapeType
	#
	self.FolderShape=''
	##
	# FolderIds property
	#
	# @var EWSType_NonEmptyArrayOfBaseFolderIdsType
	#
	self.FolderIds=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'FolderShape',
		'required' : False,
		'type' : 'FolderResponseShapeType',
		},
		{'name' : 'FolderIds',
		'required' : False,
		'type' : 'NonEmptyArrayOfBaseFolderIdsType',
		},
		]
# end this->schema
# end function __construct()
# end class GetFolderType
