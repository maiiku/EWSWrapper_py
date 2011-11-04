##
# Definition of the AbsoluteMonthlyRecurrencePatternType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the AbsoluteMonthlyRecurrencePatternType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_AbsoluteMonthlyRecurrencePatternType (EWSType):
	##
	# DayOfMonth property
	#
	# @var EWSType_int
	#
	self.DayOfMonth=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'DayOfMonth',
		'required' : False,
		'type' : 'int',
		},
		]
# end this->schema
# end function __construct()
# end class AbsoluteMonthlyRecurrencePatternType
