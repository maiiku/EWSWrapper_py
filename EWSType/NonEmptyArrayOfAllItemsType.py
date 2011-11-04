##
# Definition of the NonEmptyArrayOfAllItemsType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the NonEmptyArrayOfAllItemsType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_NonEmptyArrayOfAllItemsType (EWSType):
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
	# ReplyToItem property
	#
	# @var EWSType_ReplyToItemType
	#
	self.ReplyToItem=''
	##
	# ForwardItem property
	#
	# @var EWSType_ForwardItemType
	#
	self.ForwardItem=''
	##
	# ReplyAllToItem property
	#
	# @var EWSType_ReplyAllToItemType
	#
	self.ReplyAllToItem=''
	##
	# AcceptItem property
	#
	# @var EWSType_AcceptItemType
	#
	self.AcceptItem=''
	##
	# TentativelyAcceptItem property
	#
	# @var EWSType_TentativelyAcceptItemType
	#
	self.TentativelyAcceptItem=''
	##
	# DeclineItem property
	#
	# @var EWSType_DeclineItemType
	#
	self.DeclineItem=''
	##
	# CancelCalendarItem property
	#
	# @var EWSType_CancelCalendarItemType
	#
	self.CancelCalendarItem=''
	##
	# RemoveItem property
	#
	# @var EWSType_RemoveItemType
	#
	self.RemoveItem=''
	##
	# SuppressReadReceipt property
	#
	# @var EWSType_SuppressReadReceiptType
	#
	self.SuppressReadReceipt=''
	##
	# PostReplyItem property
	#
	# @var EWSType_PostReplyItemType
	#
	self.PostReplyItem=''
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
		{'name' : 'ReplyToItem',
		'required' : False,
		'type' : 'ReplyToItemType',
		},
		{'name' : 'ForwardItem',
		'required' : False,
		'type' : 'ForwardItemType',
		},
		{'name' : 'ReplyAllToItem',
		'required' : False,
		'type' : 'ReplyAllToItemType',
		},
		{'name' : 'AcceptItem',
		'required' : False,
		'type' : 'AcceptItemType',
		},
		{'name' : 'TentativelyAcceptItem',
		'required' : False,
		'type' : 'TentativelyAcceptItemType',
		},
		{'name' : 'DeclineItem',
		'required' : False,
		'type' : 'DeclineItemType',
		},
		{'name' : 'CancelCalendarItem',
		'required' : False,
		'type' : 'CancelCalendarItemType',
		},
		{'name' : 'RemoveItem',
		'required' : False,
		'type' : 'RemoveItemType',
		},
		{'name' : 'SuppressReadReceipt',
		'required' : False,
		'type' : 'SuppressReadReceiptType',
		},
		{'name' : 'PostReplyItem',
		'required' : False,
		'type' : 'PostReplyItemType',
		},
		]
# end this->schema
# end function __construct()
# end class NonEmptyArrayOfAllItemsType
