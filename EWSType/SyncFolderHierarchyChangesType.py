##
# Definition of the SyncFolderHierarchyChangesType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the SyncFolderHierarchyChangesType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_SyncFolderHierarchyChangesType (EWSType):
	##
	# Create property
	#
	# @var EWSType_SyncFolderHierarchyCreateOrUpdateType
	#
	self.Create=''
	##
	# Update property
	#
	# @var EWSType_SyncFolderHierarchyCreateOrUpdateType
	#
	self.Update=''
	##
	# Delete property
	#
	# @var EWSType_SyncFolderHierarchyDeleteType
	#
	self.Delete=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'Create',
		'required' : False,
		'type' : 'SyncFolderHierarchyCreateOrUpdateType',
		},
		{'name' : 'Update',
		'required' : False,
		'type' : 'SyncFolderHierarchyCreateOrUpdateType',
		},
		{'name' : 'Delete',
		'required' : False,
		'type' : 'SyncFolderHierarchyDeleteType',
		},
		]
# end this->schema
# end function __construct()
# end class SyncFolderHierarchyChangesType
