##
# Definition of the CalendarViewType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the CalendarViewType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_CalendarViewType (EWSType):
	##
	# StartDate property
	#
	# @var EWSType_dateTime
	#
	self.StartDate=''
	##
	# EndDate property
	#
	# @var EWSType_dateTime
	#
	self.EndDate=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'StartDate',
		'required' : False,
		'type' : 'dateTime',
		},
		{'name' : 'EndDate',
		'required' : False,
		'type' : 'dateTime',
		},
		]
# end this->schema
# end function __construct()
# end class CalendarViewType
