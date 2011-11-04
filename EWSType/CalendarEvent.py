##
# Definition of the CalendarEvent type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the CalendarEvent type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_CalendarEvent (EWSType):
	##
	# StartTime property
	#
	# @var EWSType_dateTime
	#
	self.StartTime=''
	##
	# EndTime property
	#
	# @var EWSType_dateTime
	#
	self.EndTime=''
	##
	# BusyType property
	#
	# @var EWSType_LegacyFreeBusyType
	#
	self.BusyType=''
	##
	# CalendarEventDetails property
	#
	# @var EWSType_CalendarEventDetails
	#
	self.CalendarEventDetails=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'StartTime',
		'required' : False,
		'type' : 'dateTime',
		},
		{'name' : 'EndTime',
		'required' : False,
		'type' : 'dateTime',
		},
		{'name' : 'BusyType',
		'required' : False,
		'type' : 'LegacyFreeBusyType',
		},
		{'name' : 'CalendarEventDetails',
		'required' : False,
		'type' : 'CalendarEventDetails',
		},
		]
# end this->schema
# end function __construct()
# end class CalendarEvent
