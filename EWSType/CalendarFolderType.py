##
# Definition of the CalendarFolderType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the CalendarFolderType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_CalendarFolderType (EWSType):
	##
	# PermissionSet property
	#
	# @var EWSType_CalendarPermissionSetType
	#
	self.PermissionSet=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'PermissionSet',
		'required' : False,
		'type' : 'CalendarPermissionSetType',
		},
		]
# end this->schema
# end function __construct()
# end class CalendarFolderType
