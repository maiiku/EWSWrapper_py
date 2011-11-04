##
# Definition of the CalendarItemType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the CalendarItemType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_CalendarItemType (EWSType):
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
	# Start property
	#
	# @var EWSType_dateTime
	#
	self.Start=''
	##
	# End property
	#
	# @var EWSType_dateTime
	#
	self.End=''
	##
	# OriginalStart property
	#
	# @var EWSType_dateTime
	#
	self.OriginalStart=''
	##
	# IsAllDayEvent property
	#
	# @var EWSType_boolean
	#
	self.IsAllDayEvent=''
	##
	# LegacyFreeBusyStatus property
	#
	# @var EWSType_LegacyFreeBusyType
	#
	self.LegacyFreeBusyStatus=''
	##
	# Location property
	#
	# @var string
	#
	self.Location=''
	##
	# When property
	#
	# @var string
	#
	self.When=''
	##
	# IsMeeting property
	#
	# @var EWSType_boolean
	#
	self.IsMeeting=''
	##
	# IsCancelled property
	#
	# @var EWSType_boolean
	#
	self.IsCancelled=''
	##
	# IsRecurring property
	#
	# @var EWSType_boolean
	#
	self.IsRecurring=''
	##
	# MeetingRequestWasSent property
	#
	# @var EWSType_boolean
	#
	self.MeetingRequestWasSent=''
	##
	# IsResponseRequested property
	#
	# @var EWSType_boolean
	#
	self.IsResponseRequested=''
	##
	# CalendarItemType property
	#
	# @var EWSType_CalendarItemTypeType
	#
	self.CalendarItemType=''
	##
	# MyResponseType property
	#
	# @var EWSType_ResponseTypeType
	#
	self.MyResponseType=''
	##
	# Organizer property
	#
	# @var EWSType_SingleRecipientType
	#
	self.Organizer=''
	##
	# RequiredAttendees property
	#
	# @var EWSType_NonEmptyArrayOfAttendeesType
	#
	self.RequiredAttendees=''
	##
	# OptionalAttendees property
	#
	# @var EWSType_NonEmptyArrayOfAttendeesType
	#
	self.OptionalAttendees=''
	##
	# Resources property
	#
	# @var EWSType_NonEmptyArrayOfAttendeesType
	#
	self.Resources=''
	##
	# ConflictingMeetingCount property
	#
	# @var EWSType_int
	#
	self.ConflictingMeetingCount=''
	##
	# AdjacentMeetingCount property
	#
	# @var EWSType_int
	#
	self.AdjacentMeetingCount=''
	##
	# ConflictingMeetings property
	#
	# @var EWSType_NonEmptyArrayOfAllItemsType
	#
	self.ConflictingMeetings=''
	##
	# AdjacentMeetings property
	#
	# @var EWSType_NonEmptyArrayOfAllItemsType
	#
	self.AdjacentMeetings=''
	##
	# Duration property
	#
	# @var string
	#
	self.Duration=''
	##
	# TimeZone property
	#
	# @var string
	#
	self.TimeZone=''
	##
	# AppointmentReplyTime property
	#
	# @var EWSType_dateTime
	#
	self.AppointmentReplyTime=''
	##
	# AppointmentSequenceNumber property
	#
	# @var EWSType_int
	#
	self.AppointmentSequenceNumber=''
	##
	# AppointmentState property
	#
	# @var EWSType_int
	#
	self.AppointmentState=''
	##
	# Recurrence property
	#
	# @var EWSType_RecurrenceType
	#
	self.Recurrence=''
	##
	# FirstOccurrence property
	#
	# @var EWSType_OccurrenceInfoType
	#
	self.FirstOccurrence=''
	##
	# LastOccurrence property
	#
	# @var EWSType_OccurrenceInfoType
	#
	self.LastOccurrence=''
	##
	# ModifiedOccurrences property
	#
	# @var EWSType_NonEmptyArrayOfOccurrenceInfoType
	#
	self.ModifiedOccurrences=''
	##
	# DeletedOccurrences property
	#
	# @var EWSType_NonEmptyArrayOfDeletedOccurrencesType
	#
	self.DeletedOccurrences=''
	##
	# MeetingTimeZone property
	#
	# @var EWSType_TimeZoneType
	#
	self.MeetingTimeZone=''
	##
	# ConferenceType property
	#
	# @var EWSType_int
	#
	self.ConferenceType=''
	##
	# AllowNewTimeProposal property
	#
	# @var EWSType_boolean
	#
	self.AllowNewTimeProposal=''
	##
	# IsOnlineMeeting property
	#
	# @var EWSType_boolean
	#
	self.IsOnlineMeeting=''
	##
	# MeetingWorkspaceUrl property
	#
	# @var string
	#
	self.MeetingWorkspaceUrl=''
	##
	# NetShowUrl property
	#
	# @var string
	#
	self.NetShowUrl=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'UID',
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
		{'name' : 'Start',
		'required' : False,
		'type' : 'dateTime',
		},
		{'name' : 'End',
		'required' : False,
		'type' : 'dateTime',
		},
		{'name' : 'OriginalStart',
		'required' : False,
		'type' : 'dateTime',
		},
		{'name' : 'IsAllDayEvent',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'LegacyFreeBusyStatus',
		'required' : False,
		'type' : 'LegacyFreeBusyType',
		},
		{'name' : 'Location',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'When',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'IsMeeting',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'IsCancelled',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'IsRecurring',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'MeetingRequestWasSent',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'IsResponseRequested',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'CalendarItemType',
		'required' : False,
		'type' : 'CalendarItemTypeType',
		},
		{'name' : 'MyResponseType',
		'required' : False,
		'type' : 'ResponseTypeType',
		},
		{'name' : 'Organizer',
		'required' : False,
		'type' : 'SingleRecipientType',
		},
		{'name' : 'RequiredAttendees',
		'required' : False,
		'type' : 'NonEmptyArrayOfAttendeesType',
		},
		{'name' : 'OptionalAttendees',
		'required' : False,
		'type' : 'NonEmptyArrayOfAttendeesType',
		},
		{'name' : 'Resources',
		'required' : False,
		'type' : 'NonEmptyArrayOfAttendeesType',
		},
		{'name' : 'ConflictingMeetingCount',
		'required' : False,
		'type' : 'int',
		},
		{'name' : 'AdjacentMeetingCount',
		'required' : False,
		'type' : 'int',
		},
		{'name' : 'ConflictingMeetings',
		'required' : False,
		'type' : 'NonEmptyArrayOfAllItemsType',
		},
		{'name' : 'AdjacentMeetings',
		'required' : False,
		'type' : 'NonEmptyArrayOfAllItemsType',
		},
		{'name' : 'Duration',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'TimeZone',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'AppointmentReplyTime',
		'required' : False,
		'type' : 'dateTime',
		},
		{'name' : 'AppointmentSequenceNumber',
		'required' : False,
		'type' : 'int',
		},
		{'name' : 'AppointmentState',
		'required' : False,
		'type' : 'int',
		},
		{'name' : 'Recurrence',
		'required' : False,
		'type' : 'RecurrenceType',
		},
		{'name' : 'FirstOccurrence',
		'required' : False,
		'type' : 'OccurrenceInfoType',
		},
		{'name' : 'LastOccurrence',
		'required' : False,
		'type' : 'OccurrenceInfoType',
		},
		{'name' : 'ModifiedOccurrences',
		'required' : False,
		'type' : 'NonEmptyArrayOfOccurrenceInfoType',
		},
		{'name' : 'DeletedOccurrences',
		'required' : False,
		'type' : 'NonEmptyArrayOfDeletedOccurrencesType',
		},
		{'name' : 'MeetingTimeZone',
		'required' : False,
		'type' : 'TimeZoneType',
		},
		{'name' : 'ConferenceType',
		'required' : False,
		'type' : 'int',
		},
		{'name' : 'AllowNewTimeProposal',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'IsOnlineMeeting',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'MeetingWorkspaceUrl',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'NetShowUrl',
		'required' : False,
		'type' : 'string',
		},
		]
# end this->schema
# end function __construct()
# end class CalendarItemType
