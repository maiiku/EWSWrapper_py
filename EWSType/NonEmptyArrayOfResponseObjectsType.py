##
# Definition of the NonEmptyArrayOfResponseObjectsType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the NonEmptyArrayOfResponseObjectsType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_NonEmptyArrayOfResponseObjectsType (EWSType):
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
		self.schema = [{'name' : 'AcceptItem',
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
# end class NonEmptyArrayOfResponseObjectsType
