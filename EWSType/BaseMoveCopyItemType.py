##
# Definition of the BaseMoveCopyItemType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the BaseMoveCopyItemType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_BaseMoveCopyItemType (EWSType):
	##
	# ToFolderId property
	#
	# @var EWSType_TargetFolderIdType
	#
	self.ToFolderId=''
	##
	# ItemIds property
	#
	# @var EWSType_NonEmptyArrayOfBaseItemIdsType
	#
	self.ItemIds=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'ToFolderId',
		'required' : False,
		'type' : 'TargetFolderIdType',
		},
		{'name' : 'ItemIds',
		'required' : False,
		'type' : 'NonEmptyArrayOfBaseItemIdsType',
		},
		]
# end this->schema
# end function __construct()
# end class BaseMoveCopyItemType
