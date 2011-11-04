##
# Definition of the IntervalRecurrencePatternBaseType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the IntervalRecurrencePatternBaseType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_IntervalRecurrencePatternBaseType (EWSType):
	##
	# Interval property
	#
	# @var EWSType_int
	#
	self.Interval=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'Interval',
		'required' : False,
		'type' : 'int',
		},
		]
# end this->schema
# end function __construct()
# end class IntervalRecurrencePatternBaseType
