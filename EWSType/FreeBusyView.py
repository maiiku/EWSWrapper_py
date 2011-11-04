##
# Definition of the FreeBusyView type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the FreeBusyView type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_FreeBusyView (EWSType):
	##
	# FreeBusyViewType property
	#
	# @var EWSType_FreeBusyViewType
	#
	self.FreeBusyViewType=''
	##
	# MergedFreeBusy property
	#
	# @var string
	#
	self.MergedFreeBusy=''
	##
	# CalendarEventArray property
	#
	# @var EWSType_ArrayOfCalendarEvent
	#
	self.CalendarEventArray=''
	##
	# WorkingHours property
	#
	# @var EWSType_WorkingHours
	#
	self.WorkingHours=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'FreeBusyViewType',
		'required' : False,
		'type' : 'FreeBusyViewType',
		},
		{'name' : 'MergedFreeBusy',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'CalendarEventArray',
		'required' : False,
		'type' : 'ArrayOfCalendarEvent',
		},
		{'name' : 'WorkingHours',
		'required' : False,
		'type' : 'WorkingHours',
		},
		]
# end this->schema
# end function __construct()
# end class FreeBusyView
