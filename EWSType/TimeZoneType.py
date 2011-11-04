##
# Definition of the TimeZoneType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the TimeZoneType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_TimeZoneType (EWSType):
	##
	# BaseOffset property
	#
	# @var EWSType_duration
	#
	self.BaseOffset=''
	##
	# Standard property
	#
	# @var EWSType_TimeChangeType
	#
	self.Standard=''
	##
	# Daylight property
	#
	# @var EWSType_TimeChangeType
	#
	self.Daylight=''
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
		self.schema = [{'name' : 'BaseOffset',
		'required' : False,
		'type' : 'duration',
		},
		{'name' : 'Standard',
		'required' : False,
		'type' : 'TimeChangeType',
		},
		{'name' : 'Daylight',
		'required' : False,
		'type' : 'TimeChangeType',
		},
		{'name' : 'TimeZoneName',
		'required' : False,
		'type' : 'string',
		},
		]
# end this->schema
# end function __construct()
# end class TimeZoneType
