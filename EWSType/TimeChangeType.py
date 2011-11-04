##
# Definition of the TimeChangeType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the TimeChangeType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_TimeChangeType (EWSType):
	##
	# Offset property
	#
	# @var EWSType_duration
	#
	self.Offset=''
	##
	# RelativeYearlyRecurrence property
	#
	# @var EWSType_RelativeYearlyRecurrencePatternType
	#
	self.RelativeYearlyRecurrence=''
	##
	# AbsoluteDate property
	#
	# @var EWSType_date
	#
	self.AbsoluteDate=''
	##
	# Time property
	#
	# @var EWSType_time
	#
	self.Time=''
	##
	# TimeZoneName property
	#
	# @var string
	#
	self.TimeZoneName=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'Offset',
		'required' : False,
		'type' : 'duration',
		},
		{'name' : 'RelativeYearlyRecurrence',
		'required' : False,
		'type' : 'RelativeYearlyRecurrencePatternType',
		},
		{'name' : 'AbsoluteDate',
		'required' : False,
		'type' : 'date',
		},
		{'name' : 'Time',
		'required' : False,
		'type' : 'time',
		},
		{'name' : 'TimeZoneName',
		'required' : False,
		'type' : 'string',
		},
		]
# end this->schema
# end function __construct()
# end class TimeChangeType
