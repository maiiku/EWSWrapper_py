##
# Definition of the BasePermissionType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the BasePermissionType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_BasePermissionType (EWSType):
	##
	# UserId property
	#
	# @var EWSType_UserIdType
	#
	self.UserId=''
	##
	# CanCreateItems property
	#
	# @var EWSType_boolean
	#
	self.CanCreateItems=''
	##
	# CanCreateSubFolders property
	#
	# @var EWSType_boolean
	#
	self.CanCreateSubFolders=''
	##
	# IsFolderOwner property
	#
	# @var EWSType_boolean
	#
	self.IsFolderOwner=''
	##
	# IsFolderVisible property
	#
	# @var EWSType_boolean
	#
	self.IsFolderVisible=''
	##
	# IsFolderContact property
	#
	# @var EWSType_boolean
	#
	self.IsFolderContact=''
	##
	# EditItems property
	#
	# @var EWSType_PermissionActionType
	#
	self.EditItems=''
	##
	# DeleteItems property
	#
	# @var EWSType_PermissionActionType
	#
	self.DeleteItems=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'UserId',
		'required' : False,
		'type' : 'UserIdType',
		},
		{'name' : 'CanCreateItems',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'CanCreateSubFolders',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'IsFolderOwner',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'IsFolderVisible',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'IsFolderContact',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'EditItems',
		'required' : False,
		'type' : 'PermissionActionType',
		},
		{'name' : 'DeleteItems',
		'required' : False,
		'type' : 'PermissionActionType',
		},
		]
# end this->schema
# end function __construct()
# end class BasePermissionType
