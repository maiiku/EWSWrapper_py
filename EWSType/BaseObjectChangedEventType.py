##
# Definition of the BaseObjectChangedEventType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the BaseObjectChangedEventType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_BaseObjectChangedEventType (EWSType):
	##
	# TimeStamp property
	#
	# @var EWSType_dateTime
	#
	self.TimeStamp=''
	##
	# FolderId property
	#
	# @var EWSType_FolderIdType
	#
	self.FolderId=''
	##
	# ItemId property
	#
	# @var EWSType_ItemIdType
	#
	self.ItemId=''
	##
	# ParentFolderId property
	#
	# @var EWSType_FolderIdType
	#
	self.ParentFolderId=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'TimeStamp',
		'required' : False,
		'type' : 'dateTime',
		},
		{'name' : 'FolderId',
		'required' : False,
		'type' : 'FolderIdType',
		},
		{'name' : 'ItemId',
		'required' : False,
		'type' : 'ItemIdType',
		},
		{'name' : 'ParentFolderId',
		'required' : False,
		'type' : 'FolderIdType',
		},
		]
# end this->schema
# end function __construct()
# end class BaseObjectChangedEventType
