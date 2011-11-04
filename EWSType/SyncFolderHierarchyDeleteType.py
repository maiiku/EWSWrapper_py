##
# Definition of the SyncFolderHierarchyDeleteType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the SyncFolderHierarchyDeleteType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_SyncFolderHierarchyDeleteType (EWSType):
	##
	# FolderId property
	#
	# @var EWSType_FolderIdType
	#
	self.FolderId=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'FolderId',
		'required' : False,
		'type' : 'FolderIdType',
		},
		]
# end this->schema
# end function __construct()
# end class SyncFolderHierarchyDeleteType
