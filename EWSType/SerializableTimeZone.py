##
# Definition of the SerializableTimeZone type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the SerializableTimeZone type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_SerializableTimeZone (EWSType):
	##
	# Bias property
	#
	# @var EWSType_int
	#
	self.Bias=''
	##
	# StandardTime property
	#
	# @var EWSType_SerializableTimeZoneTime
	#
	self.StandardTime=''
	##
	# DaylightTime property
	#
	# @var EWSType_SerializableTimeZoneTime
	#
	self.DaylightTime=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'Bias',
		'required' : False,
		'type' : 'int',
		},
		{'name' : 'StandardTime',
		'required' : False,
		'type' : 'SerializableTimeZoneTime',
		},
		{'name' : 'DaylightTime',
		'required' : False,
		'type' : 'SerializableTimeZoneTime',
		},
		]
# end this->schema
# end function __construct()
# end class SerializableTimeZone
