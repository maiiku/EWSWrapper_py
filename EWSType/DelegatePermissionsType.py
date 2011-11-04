##
# Definition of the DelegatePermissionsType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the DelegatePermissionsType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_DelegatePermissionsType (EWSType):
	##
	# CalendarFolderPermissionLevel property
	#
	# @var EWSType_DelegateFolderPermissionLevelType
	#
	self.CalendarFolderPermissionLevel=''
	##
	# TasksFolderPermissionLevel property
	#
	# @var EWSType_DelegateFolderPermissionLevelType
	#
	self.TasksFolderPermissionLevel=''
	##
	# InboxFolderPermissionLevel property
	#
	# @var EWSType_DelegateFolderPermissionLevelType
	#
	self.InboxFolderPermissionLevel=''
	##
	# ContactsFolderPermissionLevel property
	#
	# @var EWSType_DelegateFolderPermissionLevelType
	#
	self.ContactsFolderPermissionLevel=''
	##
	# NotesFolderPermissionLevel property
	#
	# @var EWSType_DelegateFolderPermissionLevelType
	#
	self.NotesFolderPermissionLevel=''
	##
	# JournalFolderPermissionLevel property
	#
	# @var EWSType_DelegateFolderPermissionLevelType
	#
	self.JournalFolderPermissionLevel=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'CalendarFolderPermissionLevel',
		'required' : False,
		'type' : 'DelegateFolderPermissionLevelType',
		},
		{'name' : 'TasksFolderPermissionLevel',
		'required' : False,
		'type' : 'DelegateFolderPermissionLevelType',
		},
		{'name' : 'InboxFolderPermissionLevel',
		'required' : False,
		'type' : 'DelegateFolderPermissionLevelType',
		},
		{'name' : 'ContactsFolderPermissionLevel',
		'required' : False,
		'type' : 'DelegateFolderPermissionLevelType',
		},
		{'name' : 'NotesFolderPermissionLevel',
		'required' : False,
		'type' : 'DelegateFolderPermissionLevelType',
		},
		{'name' : 'JournalFolderPermissionLevel',
		'required' : False,
		'type' : 'DelegateFolderPermissionLevelType',
		},
		]
# end this->schema
# end function __construct()
# end class DelegatePermissionsType
