##
# Definition of the MovedCopiedEventType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the MovedCopiedEventType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_MovedCopiedEventType (EWSType):
	##
	# OldFolderId property
	#
	# @var EWSType_FolderIdType
	#
	self.OldFolderId=''
	##
	# OldItemId property
	#
	# @var EWSType_ItemIdType
	#
	self.OldItemId=''
	##
	# OldParentFolderId property
	#
	# @var EWSType_FolderIdType
	#
	self.OldParentFolderId=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'OldFolderId',
		'required' : False,
		'type' : 'FolderIdType',
		},
		{'name' : 'OldItemId',
		'required' : False,
		'type' : 'ItemIdType',
		},
		{'name' : 'OldParentFolderId',
		'required' : False,
		'type' : 'FolderIdType',
		},
		]
# end this->schema
# end function __construct()
# end class MovedCopiedEventType
