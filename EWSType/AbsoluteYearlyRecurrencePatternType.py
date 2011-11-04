##
# Definition of the AbsoluteYearlyRecurrencePatternType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the AbsoluteYearlyRecurrencePatternType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_AbsoluteYearlyRecurrencePatternType (EWSType):
	##
	# DayOfMonth property
	#
	# @var EWSType_int
	#
	self.DayOfMonth=''
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
		self.schema = [{'name' : 'DayOfMonth',
		'required' : False,
		'type' : 'int',
		},
		{'name' : 'Month',
		'required' : False,
		'type' : 'MonthNamesType',
		},
		]
# end this->schema
# end function __construct()
# end class AbsoluteYearlyRecurrencePatternType
