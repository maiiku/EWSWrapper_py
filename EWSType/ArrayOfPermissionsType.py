##
# Definition of the ArrayOfPermissionsType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the ArrayOfPermissionsType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_ArrayOfPermissionsType (EWSType):
	##
	# Permission property
	#
	# @var EWSType_PermissionType
	#
	self.Permission=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'Permission',
		'required' : False,
		'type' : 'PermissionType',
		},
		]
# end this->schema
# end function __construct()
# end class ArrayOfPermissionsType
