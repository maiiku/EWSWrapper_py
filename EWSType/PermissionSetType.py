##
# Definition of the PermissionSetType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the PermissionSetType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_PermissionSetType (EWSType):
	##
	# Permissions property
	#
	# @var EWSType_ArrayOfPermissionsType
	#
	self.Permissions=''
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
		self.schema = [{'name' : 'Permissions',
		'required' : False,
		'type' : 'ArrayOfPermissionsType',
		},
		{'name' : 'UnknownEntries',
		'required' : False,
		'type' : 'ArrayOfUnknownEntriesType',
		},
		]
# end this->schema
# end function __construct()
# end class PermissionSetType
