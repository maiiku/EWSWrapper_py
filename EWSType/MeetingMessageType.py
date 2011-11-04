##
# Definition of the MeetingMessageType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the MeetingMessageType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_MeetingMessageType (EWSType):
	##
	# AssociatedCalendarItemId property
	#
	# @var EWSType_ItemIdType
	#
	self.AssociatedCalendarItemId=''
	##
	# IsDelegated property
	#
	# @var EWSType_boolean
	#
	self.IsDelegated=''
	##
	# IsOutOfDate property
	#
	# @var EWSType_boolean
	#
	self.IsOutOfDate=''
	##
	# HasBeenProcessed property
	#
	# @var EWSType_boolean
	#
	self.HasBeenProcessed=''
	##
	# ResponseType property
	#
	# @var EWSType_ResponseTypeType
	#
	self.ResponseType=''
	##
	# UID property
	#
	# @var string
	#
	self.UID=''
	##
	# RecurrenceId property
	#
	# @var EWSType_dateTime
	#
	self.RecurrenceId=''
	##
	# DateTimeStamp property
	#
	# @var EWSType_dateTime
	#
	self.DateTimeStamp=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'AssociatedCalendarItemId',
		'required' : False,
		'type' : 'ItemIdType',
		},
		{'name' : 'IsDelegated',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'IsOutOfDate',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'HasBeenProcessed',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'ResponseType',
		'required' : False,
		'type' : 'ResponseTypeType',
		},
		{'name' : 'UID',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'RecurrenceId',
		'required' : False,
		'type' : 'dateTime',
		},
		{'name' : 'DateTimeStamp',
		'required' : False,
		'type' : 'dateTime',
		},
		]
# end this->schema
# end function __construct()
# end class MeetingMessageType
