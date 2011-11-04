##
# Definition of the SyncFolderItemsChangesType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the SyncFolderItemsChangesType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_SyncFolderItemsChangesType (EWSType):
	##
	# Create property
	#
	# @var EWSType_SyncFolderItemsCreateOrUpdateType
	#
	self.Create=''
	##
	# Update property
	#
	# @var EWSType_SyncFolderItemsCreateOrUpdateType
	#
	self.Update=''
	##
	# Delete property
	#
	# @var EWSType_SyncFolderItemsDeleteType
	#
	self.Delete=''
	##
	# ReadFlagChange property
	#
	# @var EWSType_SyncFolderItemsReadFlagType
	#
	self.ReadFlagChange=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'Create',
		'required' : False,
		'type' : 'SyncFolderItemsCreateOrUpdateType',
		},
		{'name' : 'Update',
		'required' : False,
		'type' : 'SyncFolderItemsCreateOrUpdateType',
		},
		{'name' : 'Delete',
		'required' : False,
		'type' : 'SyncFolderItemsDeleteType',
		},
		{'name' : 'ReadFlagChange',
		'required' : False,
		'type' : 'SyncFolderItemsReadFlagType',
		},
		]
# end this->schema
# end function __construct()
# end class SyncFolderItemsChangesType
