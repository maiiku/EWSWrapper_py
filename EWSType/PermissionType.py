##
# Definition of the PermissionType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the PermissionType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_PermissionType (EWSType):
	##
	# ReadItems property
	#
	# @var EWSType_PermissionReadAccessType
	#
	self.ReadItems=''
	##
	# PermissionLevel property
	#
	# @var EWSType_PermissionLevelType
	#
	self.PermissionLevel=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'ReadItems',
		'required' : False,
		'type' : 'PermissionReadAccessType',
		},
		{'name' : 'PermissionLevel',
		'required' : False,
		'type' : 'PermissionLevelType',
		},
		]
# end this->schema
# end function __construct()
# end class PermissionType
