##
# Definition of the BaseFolderType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the BaseFolderType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_BaseFolderType (EWSType):
	##
	# FolderId property
	#
	# @var EWSType_FolderIdType
	#
	self.FolderId=''
	##
	# ParentFolderId property
	#
	# @var EWSType_FolderIdType
	#
	self.ParentFolderId=''
	##
	# FolderClass property
	#
	# @var string
	#
	self.FolderClass=''
	##
	# DisplayName property
	#
	# @var string
	#
	self.DisplayName=''
	##
	# TotalCount property
	#
	# @var EWSType_int
	#
	self.TotalCount=''
	##
	# ChildFolderCount property
	#
	# @var EWSType_int
	#
	self.ChildFolderCount=''
	##
	# ExtendedProperty property
	#
	# @var EWSType_ExtendedPropertyType
	#
	self.ExtendedProperty=''
	##
	# ManagedFolderInformation property
	#
	# @var EWSType_ManagedFolderInformationType
	#
	self.ManagedFolderInformation=''
	##
	# EffectiveRights property
	#
	# @var EWSType_EffectiveRightsType
	#
	self.EffectiveRights=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'FolderId',
		'required' : False,
		'type' : 'FolderIdType',
		},
		{'name' : 'ParentFolderId',
		'required' : False,
		'type' : 'FolderIdType',
		},
		{'name' : 'FolderClass',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'DisplayName',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'TotalCount',
		'required' : False,
		'type' : 'int',
		},
		{'name' : 'ChildFolderCount',
		'required' : False,
		'type' : 'int',
		},
		{'name' : 'ExtendedProperty',
		'required' : False,
		'type' : 'ExtendedPropertyType',
		},
		{'name' : 'ManagedFolderInformation',
		'required' : False,
		'type' : 'ManagedFolderInformationType',
		},
		{'name' : 'EffectiveRights',
		'required' : False,
		'type' : 'EffectiveRightsType',
		},
		]
# end this->schema
# end function __construct()
# end class BaseFolderType
