##
# Definition of the SyncFolderItemsType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the SyncFolderItemsType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_SyncFolderItemsType (EWSType):
	##
	# ItemShape property
	#
	# @var EWSType_ItemResponseShapeType
	#
	self.ItemShape=''
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
	# Ignore property
	#
	# @var EWSType_ArrayOfBaseItemIdsType
	#
	self.Ignore=''
	##
	# MaxChangesReturned property
	#
	# @var EWSType_MaxSyncChangesReturnedType
	#
	self.MaxChangesReturned=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'ItemShape',
		'required' : False,
		'type' : 'ItemResponseShapeType',
		},
		{'name' : 'SyncFolderId',
		'required' : False,
		'type' : 'TargetFolderIdType',
		},
		{'name' : 'SyncState',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'Ignore',
		'required' : False,
		'type' : 'ArrayOfBaseItemIdsType',
		},
		{'name' : 'MaxChangesReturned',
		'required' : False,
		'type' : 'MaxSyncChangesReturnedType',
		},
		]
# end this->schema
# end function __construct()
# end class SyncFolderItemsType
