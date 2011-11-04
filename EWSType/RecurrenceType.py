##
# Definition of the RecurrenceType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the RecurrenceType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_RecurrenceType (EWSType):
	##
	# RelativeYearlyRecurrence property
	#
	# @var EWSType_RelativeYearlyRecurrencePatternType
	#
	self.RelativeYearlyRecurrence=''
	##
	# AbsoluteYearlyRecurrence property
	#
	# @var EWSType_AbsoluteYearlyRecurrencePatternType
	#
	self.AbsoluteYearlyRecurrence=''
	##
	# RelativeMonthlyRecurrence property
	#
	# @var EWSType_RelativeMonthlyRecurrencePatternType
	#
	self.RelativeMonthlyRecurrence=''
	##
	# AbsoluteMonthlyRecurrence property
	#
	# @var EWSType_AbsoluteMonthlyRecurrencePatternType
	#
	self.AbsoluteMonthlyRecurrence=''
	##
	# WeeklyRecurrence property
	#
	# @var EWSType_WeeklyRecurrencePatternType
	#
	self.WeeklyRecurrence=''
	##
	# DailyRecurrence property
	#
	# @var EWSType_DailyRecurrencePatternType
	#
	self.DailyRecurrence=''
	##
	# NoEndRecurrence property
	#
	# @var EWSType_NoEndRecurrenceRangeType
	#
	self.NoEndRecurrence=''
	##
	# EndDateRecurrence property
	#
	# @var EWSType_EndDateRecurrenceRangeType
	#
	self.EndDateRecurrence=''
	##
	# NumberedRecurrence property
	#
	# @var EWSType_NumberedRecurrenceRangeType
	#
	self.NumberedRecurrence=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'RelativeYearlyRecurrence',
		'required' : False,
		'type' : 'RelativeYearlyRecurrencePatternType',
		},
		{'name' : 'AbsoluteYearlyRecurrence',
		'required' : False,
		'type' : 'AbsoluteYearlyRecurrencePatternType',
		},
		{'name' : 'RelativeMonthlyRecurrence',
		'required' : False,
		'type' : 'RelativeMonthlyRecurrencePatternType',
		},
		{'name' : 'AbsoluteMonthlyRecurrence',
		'required' : False,
		'type' : 'AbsoluteMonthlyRecurrencePatternType',
		},
		{'name' : 'WeeklyRecurrence',
		'required' : False,
		'type' : 'WeeklyRecurrencePatternType',
		},
		{'name' : 'DailyRecurrence',
		'required' : False,
		'type' : 'DailyRecurrencePatternType',
		},
		{'name' : 'NoEndRecurrence',
		'required' : False,
		'type' : 'NoEndRecurrenceRangeType',
		},
		{'name' : 'EndDateRecurrence',
		'required' : False,
		'type' : 'EndDateRecurrenceRangeType',
		},
		{'name' : 'NumberedRecurrence',
		'required' : False,
		'type' : 'NumberedRecurrenceRangeType',
		},
		]
# end this->schema
# end function __construct()
# end class RecurrenceType
