##
# Definition of the WeeklyRecurrencePatternType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the WeeklyRecurrencePatternType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_WeeklyRecurrencePatternType (EWSType):
	##
	# DaysOfWeek property
	#
	# @var EWSType_DaysOfWeekType
	#
	self.DaysOfWeek=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'DaysOfWeek',
		'required' : False,
		'type' : 'DaysOfWeekType',
		},
		]
# end this->schema
# end function __construct()
# end class WeeklyRecurrencePatternType
