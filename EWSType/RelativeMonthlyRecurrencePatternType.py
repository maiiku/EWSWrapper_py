##
# Definition of the RelativeMonthlyRecurrencePatternType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the RelativeMonthlyRecurrencePatternType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_RelativeMonthlyRecurrencePatternType (EWSType):
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
		]
# end this->schema
# end function __construct()
# end class RelativeMonthlyRecurrencePatternType
