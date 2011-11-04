##
# Definition of the SyncFolderHierarchyCreateOrUpdateType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the SyncFolderHierarchyCreateOrUpdateType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_SyncFolderHierarchyCreateOrUpdateType (EWSType):
	##
	# Folder property
	#
	# @var EWSType_FolderType
	#
	self.Folder=''
	##
	# CalendarFolder property
	#
	# @var EWSType_CalendarFolderType
	#
	self.CalendarFolder=''
	##
	# ContactsFolder property
	#
	# @var EWSType_ContactsFolderType
	#
	self.ContactsFolder=''
	##
	# SearchFolder property
	#
	# @var EWSType_SearchFolderType
	#
	self.SearchFolder=''
	##
	# TasksFolder property
	#
	# @var EWSType_TasksFolderType
	#
	self.TasksFolder=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'Folder',
		'required' : False,
		'type' : 'FolderType',
		},
		{'name' : 'CalendarFolder',
		'required' : False,
		'type' : 'CalendarFolderType',
		},
		{'name' : 'ContactsFolder',
		'required' : False,
		'type' : 'ContactsFolderType',
		},
		{'name' : 'SearchFolder',
		'required' : False,
		'type' : 'SearchFolderType',
		},
		{'name' : 'TasksFolder',
		'required' : False,
		'type' : 'TasksFolderType',
		},
		]
# end this->schema
# end function __construct()
# end class SyncFolderHierarchyCreateOrUpdateType
