##
# Definition of the RelativeYearlyRecurrencePatternType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the RelativeYearlyRecurrencePatternType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_RelativeYearlyRecurrencePatternType (EWSType):
	##
	# DaysOfWeek property
	#
	# @var EWSType_DayOfWeekType
	#
	self.DaysOfWeek=''
	##
	# DayOfWeekIndex property
	#
	# @var EWSType_DayOfWeekIndexType
	#
	self.DayOfWeekIndex=''
	##
	# Month property
	#
	# @var EWSType_MonthNamesType
	#
	self.Month=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'DaysOfWeek',
		'required' : False,
		'type' : 'DayOfWeekType',
		},
		{'name' : 'DayOfWeekIndex',
		'required' : False,
		'type' : 'DayOfWeekIndexType',
		},
		{'name' : 'Month',
		'required' : False,
		'type' : 'MonthNamesType',
		},
		]
# end this->schema
# end function __construct()
# end class RelativeYearlyRecurrencePatternType
