##
# Definition of the WorkingPeriod type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the WorkingPeriod type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_WorkingPeriod (EWSType):
	##
	# DayOfWeek property
	#
	# @var EWSType_DaysOfWeekType
	#
	self.DayOfWeek=''
	##
	# StartTimeInMinutes property
	#
	# @var EWSType_int
	#
	self.StartTimeInMinutes=''
	##
	# EndTimeInMinutes property
	#
	# @var EWSType_int
	#
	self.EndTimeInMinutes=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'DayOfWeek',
		'required' : False,
		'type' : 'DaysOfWeekType',
		},
		{'name' : 'StartTimeInMinutes',
		'required' : False,
		'type' : 'int',
		},
		{'name' : 'EndTimeInMinutes',
		'required' : False,
		'type' : 'int',
		},
		]
# end this->schema
# end function __construct()
# end class WorkingPeriod
