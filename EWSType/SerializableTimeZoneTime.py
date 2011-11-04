##
# Definition of the SerializableTimeZoneTime type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the SerializableTimeZoneTime type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_SerializableTimeZoneTime (EWSType):
	##
	# Bias property
	#
	# @var EWSType_int
	#
	self.Bias=''
	##
	# Time property
	#
	# @var string
	#
	self.Time=''
	##
	# DayOrder property
	#
	# @var EWSType_short
	#
	self.DayOrder=''
	##
	# Month property
	#
	# @var EWSType_short
	#
	self.Month=''
	##
	# DayOfWeek property
	#
	# @var EWSType_DayOfWeekType
	#
	self.DayOfWeek=''
	##
	# Year property
	#
	# @var string
	#
	self.Year=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'Bias',
		'required' : False,
		'type' : 'int',
		},
		{'name' : 'Time',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'DayOrder',
		'required' : False,
		'type' : 'short',
		},
		{'name' : 'Month',
		'required' : False,
		'type' : 'short',
		},
		{'name' : 'DayOfWeek',
		'required' : False,
		'type' : 'DayOfWeekType',
		},
		{'name' : 'Year',
		'required' : False,
		'type' : 'string',
		},
		]
# end this->schema
# end function __construct()
# end class SerializableTimeZoneTime
