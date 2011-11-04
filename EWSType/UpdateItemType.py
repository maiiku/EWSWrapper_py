##
# Definition of the UpdateItemType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the UpdateItemType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_UpdateItemType (EWSType):
	##
	# SavedItemFolderId property
	#
	# @var EWSType_TargetFolderIdType
	#
	self.SavedItemFolderId=''
	##
	# ItemChanges property
	#
	# @var EWSType_NonEmptyArrayOfItemChangesType
	#
	self.ItemChanges=''
	##
	# ConflictResolution property
	#
	# @var EWSType_ConflictResolutionType
	#
	self.ConflictResolution=''
	##
	# MessageDisposition property
	#
	# @var EWSType_MessageDispositionType
	#
	self.MessageDisposition=''
	##
	# SendMeetingInvitationsOrCancellations property
	#
	# @var EWSType_CalendarItemUpdateOperationType
	#
	self.SendMeetingInvitationsOrCancellations=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'SavedItemFolderId',
		'required' : False,
		'type' : 'TargetFolderIdType',
		},
		{'name' : 'ItemChanges',
		'required' : False,
		'type' : 'NonEmptyArrayOfItemChangesType',
		},
		{'name' : 'ConflictResolution',
		'required' : False,
		'type' : 'ConflictResolutionType',
		},
		{'name' : 'MessageDisposition',
		'required' : False,
		'type' : 'MessageDispositionType',
		},
		{'name' : 'SendMeetingInvitationsOrCancellations',
		'required' : False,
		'type' : 'CalendarItemUpdateOperationType',
		},
		]
# end this->schema
# end function __construct()
# end class UpdateItemType
