##
# Definition of the FindFolderType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the FindFolderType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_FindFolderType (EWSType):
	##
	# FolderShape property
	#
	# @var EWSType_FolderResponseShapeType
	#
	self.FolderShape=''
	##
	# IndexedPageFolderView property
	#
	# @var EWSType_IndexedPageViewType
	#
	self.IndexedPageFolderView=''
	##
	# FractionalPageFolderView property
	#
	# @var EWSType_FractionalPageViewType
	#
	self.FractionalPageFolderView=''
	##
	# Restriction property
	#
	# @var EWSType_RestrictionType
	#
	self.Restriction=''
	##
	# ParentFolderIds property
	#
	# @var EWSType_NonEmptyArrayOfBaseFolderIdsType
	#
	self.ParentFolderIds=''
	##
	# Traversal property
	#
	# @var EWSType_FolderQueryTraversalType
	#
	self.Traversal=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'FolderShape',
		'required' : True,
		'type' : 'FolderResponseShapeType',
		},
		{'name' : 'IndexedPageFolderView',
		'required' : False,
		'type' : 'IndexedPageViewType',
		},
		{'name' : 'FractionalPageFolderView',
		'required' : False,
		'type' : 'FractionalPageViewType',
		},
		{'name' : 'Restriction',
		'required' : False,
		'type' : 'RestrictionType',
		},
		{'name' : 'ParentFolderIds',
		'required' : True,
		'type' : 'NonEmptyArrayOfBaseFolderIdsType',
		},
		{'name' : 'Traversal',
		'required' : True,
		'type' : 'FolderQueryTraversalType',
		},
		]
# end this->schema
# end function __construct()
# end class FindFolderType
