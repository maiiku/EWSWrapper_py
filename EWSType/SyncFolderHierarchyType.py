##
# Definition of the SyncFolderHierarchyType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the SyncFolderHierarchyType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_SyncFolderHierarchyType (EWSType):
	##
	# FolderShape property
	#
	# @var EWSType_FolderResponseShapeType
	#
	self.FolderShape=''
	##
	# SyncFolderId property
	#
	# @var EWSType_TargetFolderIdType
	#
	self.SyncFolderId=''
	##
	# SyncState property
	#
	# @var string
	#
	self.SyncState=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'FolderShape',
		'required' : False,
		'type' : 'FolderResponseShapeType',
		},
		{'name' : 'SyncFolderId',
		'required' : False,
		'type' : 'TargetFolderIdType',
		},
		{'name' : 'SyncState',
		'required' : False,
		'type' : 'string',
		},
		]
# end this->schema
# end function __construct()
# end class SyncFolderHierarchyType
