##
# Definition of the SendItemType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the SendItemType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_SendItemType (EWSType):
	##
	# ItemIds property
	#
	# @var EWSType_NonEmptyArrayOfBaseItemIdsType
	#
	self.ItemIds=''
	##
	# SavedItemFolderId property
	#
	# @var EWSType_TargetFolderIdType
	#
	self.SavedItemFolderId=''
	##
	# SaveItemToFolder property
	#
	# @var EWSType_boolean
	#
	self.SaveItemToFolder=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'ItemIds',
		'required' : False,
		'type' : 'NonEmptyArrayOfBaseItemIdsType',
		},
		{'name' : 'SavedItemFolderId',
		'required' : False,
		'type' : 'TargetFolderIdType',
		},
		{'name' : 'SaveItemToFolder',
		'required' : False,
		'type' : 'boolean',
		},
		]
# end this->schema
# end function __construct()
# end class SendItemType
