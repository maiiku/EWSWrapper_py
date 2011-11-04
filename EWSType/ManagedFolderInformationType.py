##
# Definition of the ManagedFolderInformationType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the ManagedFolderInformationType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_ManagedFolderInformationType (EWSType):
	##
	# CanDelete property
	#
	# @var EWSType_boolean
	#
	self.CanDelete=''
	##
	# CanRenameOrMove property
	#
	# @var EWSType_boolean
	#
	self.CanRenameOrMove=''
	##
	# MustDisplayComment property
	#
	# @var EWSType_boolean
	#
	self.MustDisplayComment=''
	##
	# HasQuota property
	#
	# @var EWSType_boolean
	#
	self.HasQuota=''
	##
	# IsManagedFoldersRoot property
	#
	# @var EWSType_boolean
	#
	self.IsManagedFoldersRoot=''
	##
	# ManagedFolderId property
	#
	# @var string
	#
	self.ManagedFolderId=''
	##
	# Comment property
	#
	# @var string
	#
	self.Comment=''
	##
	# StorageQuota property
	#
	# @var EWSType_int
	#
	self.StorageQuota=''
	##
	# FolderSize property
	#
	# @var EWSType_int
	#
	self.FolderSize=''
	##
	# HomePage property
	#
	# @var string
	#
	self.HomePage=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'CanDelete',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'CanRenameOrMove',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'MustDisplayComment',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'HasQuota',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'IsManagedFoldersRoot',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'ManagedFolderId',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'Comment',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'StorageQuota',
		'required' : False,
		'type' : 'int',
		},
		{'name' : 'FolderSize',
		'required' : False,
		'type' : 'int',
		},
		{'name' : 'HomePage',
		'required' : False,
		'type' : 'string',
		},
		]
# end this->schema
# end function __construct()
# end class ManagedFolderInformationType
