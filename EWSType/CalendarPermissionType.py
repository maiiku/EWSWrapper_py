##
# Definition of the CalendarPermissionType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the CalendarPermissionType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_CalendarPermissionType (EWSType):
	##
	# ReadItems property
	#
	# @var EWSType_CalendarPermissionReadAccessType
	#
	self.ReadItems=''
	##
	# CalendarPermissionLevel property
	#
	# @var EWSType_CalendarPermissionLevelType
	#
	self.CalendarPermissionLevel=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'ReadItems',
		'required' : False,
		'type' : 'CalendarPermissionReadAccessType',
		},
		{'name' : 'CalendarPermissionLevel',
		'required' : False,
		'type' : 'CalendarPermissionLevelType',
		},
		]
# end this->schema
# end function __construct()
# end class CalendarPermissionType
