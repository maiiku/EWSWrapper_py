##
# Definition of the SyncFolderItemsCreateOrUpdateType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the SyncFolderItemsCreateOrUpdateType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_SyncFolderItemsCreateOrUpdateType (EWSType):
	##
	# Item property
	#
	# @var EWSType_ItemType
	#
	self.Item=''
	##
	# Message property
	#
	# @var EWSType_MessageType
	#
	self.Message=''
	##
	# CalendarItem property
	#
	# @var EWSType_CalendarItemType
	#
	self.CalendarItem=''
	##
	# Contact property
	#
	# @var EWSType_ContactItemType
	#
	self.Contact=''
	##
	# DistributionList property
	#
	# @var EWSType_DistributionListType
	#
	self.DistributionList=''
	##
	# MeetingMessage property
	#
	# @var EWSType_MeetingMessageType
	#
	self.MeetingMessage=''
	##
	# MeetingRequest property
	#
	# @var EWSType_MeetingRequestMessageType
	#
	self.MeetingRequest=''
	##
	# MeetingResponse property
	#
	# @var EWSType_MeetingResponseMessageType
	#
	self.MeetingResponse=''
	##
	# MeetingCancellation property
	#
	# @var EWSType_MeetingCancellationMessageType
	#
	self.MeetingCancellation=''
	##
	# Task property
	#
	# @var EWSType_TaskType
	#
	self.Task=''
	##
	# PostItem property
	#
	# @var EWSType_PostItemType
	#
	self.PostItem=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'Item',
		'required' : False,
		'type' : 'ItemType',
		},
		{'name' : 'Message',
		'required' : False,
		'type' : 'MessageType',
		},
		{'name' : 'CalendarItem',
		'required' : False,
		'type' : 'CalendarItemType',
		},
		{'name' : 'Contact',
		'required' : False,
		'type' : 'ContactItemType',
		},
		{'name' : 'DistributionList',
		'required' : False,
		'type' : 'DistributionListType',
		},
		{'name' : 'MeetingMessage',
		'required' : False,
		'type' : 'MeetingMessageType',
		},
		{'name' : 'MeetingRequest',
		'required' : False,
		'type' : 'MeetingRequestMessageType',
		},
		{'name' : 'MeetingResponse',
		'required' : False,
		'type' : 'MeetingResponseMessageType',
		},
		{'name' : 'MeetingCancellation',
		'required' : False,
		'type' : 'MeetingCancellationMessageType',
		},
		{'name' : 'Task',
		'required' : False,
		'type' : 'TaskType',
		},
		{'name' : 'PostItem',
		'required' : False,
		'type' : 'PostItemType',
		},
		]
# end this->schema
# end function __construct()
# end class SyncFolderItemsCreateOrUpdateType
