##
# Definition of the NotificationType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the NotificationType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_NotificationType (EWSType):
	##
	# SubscriptionId property
	#
	# @var EWSType_SubscriptionIdType
	#
	self.SubscriptionId=''
	##
	# PreviousWatermark property
	#
	# @var EWSType_WatermarkType
	#
	self.PreviousWatermark=''
	##
	# MoreEvents property
	#
	# @var EWSType_boolean
	#
	self.MoreEvents=''
	##
	# CopiedEvent property
	#
	# @var EWSType_MovedCopiedEventType
	#
	self.CopiedEvent=''
	##
	# CreatedEvent property
	#
	# @var EWSType_BaseObjectChangedEventType
	#
	self.CreatedEvent=''
	##
	# DeletedEvent property
	#
	# @var EWSType_BaseObjectChangedEventType
	#
	self.DeletedEvent=''
	##
	# ModifiedEvent property
	#
	# @var EWSType_ModifiedEventType
	#
	self.ModifiedEvent=''
	##
	# MovedEvent property
	#
	# @var EWSType_MovedCopiedEventType
	#
	self.MovedEvent=''
	##
	# NewMailEvent property
	#
	# @var EWSType_BaseObjectChangedEventType
	#
	self.NewMailEvent=''
	##
	# StatusEvent property
	#
	# @var EWSType_BaseNotificationEventType
	#
	self.StatusEvent=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'SubscriptionId',
		'required' : False,
		'type' : 'SubscriptionIdType',
		},
		{'name' : 'PreviousWatermark',
		'required' : False,
		'type' : 'WatermarkType',
		},
		{'name' : 'MoreEvents',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'CopiedEvent',
		'required' : False,
		'type' : 'MovedCopiedEventType',
		},
		{'name' : 'CreatedEvent',
		'required' : False,
		'type' : 'BaseObjectChangedEventType',
		},
		{'name' : 'DeletedEvent',
		'required' : False,
		'type' : 'BaseObjectChangedEventType',
		},
		{'name' : 'ModifiedEvent',
		'required' : False,
		'type' : 'ModifiedEventType',
		},
		{'name' : 'MovedEvent',
		'required' : False,
		'type' : 'MovedCopiedEventType',
		},
		{'name' : 'NewMailEvent',
		'required' : False,
		'type' : 'BaseObjectChangedEventType',
		},
		{'name' : 'StatusEvent',
		'required' : False,
		'type' : 'BaseNotificationEventType',
		},
		]
# end this->schema
# end function __construct()
# end class NotificationType
