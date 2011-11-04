##
# Definition of the CalendarEventDetails type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the CalendarEventDetails type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_CalendarEventDetails (EWSType):
	##
	# ID property
	#
	# @var string
	#
	self.ID=''
	##
	# Subject property
	#
	# @var string
	#
	self.Subject=''
	##
	# Location property
	#
	# @var string
	#
	self.Location=''
	##
	# IsMeeting property
	#
	# @var EWSType_boolean
	#
	self.IsMeeting=''
	##
	# IsRecurring property
	#
	# @var EWSType_boolean
	#
	self.IsRecurring=''
	##
	# IsException property
	#
	# @var EWSType_boolean
	#
	self.IsException=''
	##
	# IsReminderSet property
	#
	# @var EWSType_boolean
	#
	self.IsReminderSet=''
	##
	# IsPrivate property
	#
	# @var EWSType_boolean
	#
	self.IsPrivate=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'ID',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'Subject',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'Location',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'IsMeeting',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'IsRecurring',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'IsException',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'IsReminderSet',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'IsPrivate',
		'required' : False,
		'type' : 'boolean',
		},
		]
# end this->schema
# end function __construct()
# end class CalendarEventDetails
