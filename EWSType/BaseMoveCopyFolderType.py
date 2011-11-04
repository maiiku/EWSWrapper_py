##
# Definition of the BaseMoveCopyFolderType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the BaseMoveCopyFolderType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_BaseMoveCopyFolderType (EWSType):
	##
	# ToFolderId property
	#
	# @var EWSType_TargetFolderIdType
	#
	self.ToFolderId=''
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
		self.schema = [{'name' : 'ToFolderId',
		'required' : False,
		'type' : 'TargetFolderIdType',
		},
		{'name' : 'FolderIds',
		'required' : False,
		'type' : 'NonEmptyArrayOfBaseFolderIdsType',
		},
		]
# end this->schema
# end function __construct()
# end class BaseMoveCopyFolderType
