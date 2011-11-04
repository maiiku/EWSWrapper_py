##
# Definition of the CreateItemType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the CreateItemType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_CreateItemType (EWSType):
	##
	# SavedItemFolderId property
	#
	# @var EWSType_TargetFolderIdType
	#
	self.SavedItemFolderId=''
	##
	# Items property
	#
	# @var EWSType_NonEmptyArrayOfAllItemsType
	#
	self.Items=''
	##
	# MessageDisposition property
	#
	# @var EWSType_MessageDispositionType
	#
	self.MessageDisposition=''
	##
	# SendMeetingInvitations property
	#
	# @var EWSType_CalendarItemCreateOrDeleteOperationType
	#
	self.SendMeetingInvitations=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'SavedItemFolderId',
		'required' : False,
		'type' : 'TargetFolderIdType',
		},
		{'name' : 'Items',
		'required' : False,
		'type' : 'NonEmptyArrayOfAllItemsType',
		},
		{'name' : 'MessageDisposition',
		'required' : False,
		'type' : 'MessageDispositionType',
		},
		{'name' : 'SendMeetingInvitations',
		'required' : False,
		'type' : 'CalendarItemCreateOrDeleteOperationType',
		},
		]
# end this->schema
# end function __construct()
# end class CreateItemType
