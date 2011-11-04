##
# Definition of the CalendarPermissionSetType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the CalendarPermissionSetType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_CalendarPermissionSetType (EWSType):
	##
	# CalendarPermissions property
	#
	# @var EWSType_ArrayOfCalendarPermissionsType
	#
	self.CalendarPermissions=''
	##
	# UnknownEntries property
	#
	# @var EWSType_ArrayOfUnknownEntriesType
	#
	self.UnknownEntries=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'CalendarPermissions',
		'required' : False,
		'type' : 'ArrayOfCalendarPermissionsType',
		},
		{'name' : 'UnknownEntries',
		'required' : False,
		'type' : 'ArrayOfUnknownEntriesType',
		},
		]
# end this->schema
# end function __construct()
# end class CalendarPermissionSetType
