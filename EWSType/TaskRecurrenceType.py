##
# Definition of the TaskRecurrenceType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the TaskRecurrenceType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_TaskRecurrenceType (EWSType):
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
	# DailyRegeneration property
	#
	# @var EWSType_DailyRegeneratingPatternType
	#
	self.DailyRegeneration=''
	##
	# WeeklyRegeneration property
	#
	# @var EWSType_WeeklyRegeneratingPatternType
	#
	self.WeeklyRegeneration=''
	##
	# MonthlyRegeneration property
	#
	# @var EWSType_MonthlyRegeneratingPatternType
	#
	self.MonthlyRegeneration=''
	##
	# YearlyRegeneration property
	#
	# @var EWSType_YearlyRegeneratingPatternType
	#
	self.YearlyRegeneration=''
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
		{'name' : 'DailyRegeneration',
		'required' : False,
		'type' : 'DailyRegeneratingPatternType',
		},
		{'name' : 'WeeklyRegeneration',
		'required' : False,
		'type' : 'WeeklyRegeneratingPatternType',
		},
		{'name' : 'MonthlyRegeneration',
		'required' : False,
		'type' : 'MonthlyRegeneratingPatternType',
		},
		{'name' : 'YearlyRegeneration',
		'required' : False,
		'type' : 'YearlyRegeneratingPatternType',
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
# end class TaskRecurrenceType
