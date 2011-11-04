##
# Definition of the ArrayOfCalendarPermissionsType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the ArrayOfCalendarPermissionsType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_ArrayOfCalendarPermissionsType (EWSType):
	##
	# CalendarPermission property
	#
	# @var EWSType_CalendarPermissionType
	#
	self.CalendarPermission=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'CalendarPermission',
		'required' : False,
		'type' : 'CalendarPermissionType',
		},
		]
# end this->schema
# end function __construct()
# end class ArrayOfCalendarPermissionsType
