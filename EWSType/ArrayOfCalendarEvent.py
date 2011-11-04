##
# Definition of the ArrayOfCalendarEvent type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the ArrayOfCalendarEvent type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_ArrayOfCalendarEvent (EWSType):
	##
	# CalendarEvent property
	#
	# @var EWSType_CalendarEvent
	#
	self.CalendarEvent=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'CalendarEvent',
		'required' : False,
		'type' : 'CalendarEvent',
		},
		]
# end this->schema
# end function __construct()
# end class ArrayOfCalendarEvent
