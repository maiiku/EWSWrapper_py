##
# Definition of the FindItemType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the FindItemType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_FindItemType (EWSType):
	##
	# ItemShape property
	#
	# @var EWSType_ItemResponseShapeType
	#
	self.ItemShape=''
	##
	# IndexedPageItemView property
	#
	# @var EWSType_IndexedPageViewType
	#
	self.IndexedPageItemView=''
	##
	# FractionalPageItemView property
	#
	# @var EWSType_FractionalPageViewType
	#
	self.FractionalPageItemView=''
	##
	# CalendarView property
	#
	# @var EWSType_CalendarViewType
	#
	self.CalendarView=''
	##
	# ContactsView property
	#
	# @var EWSType_ContactsViewType
	#
	self.ContactsView=''
	##
	# GroupBy property
	#
	# @var EWSType_GroupByType
	#
	self.GroupBy=''
	##
	# DistinguishedGroupBy property
	#
	# @var EWSType_DistinguishedGroupByType
	#
	self.DistinguishedGroupBy=''
	##
	# Restriction property
	#
	# @var EWSType_RestrictionType
	#
	self.Restriction=''
	##
	# SortOrder property
	#
	# @var EWSType_NonEmptyArrayOfFieldOrdersType
	#
	self.SortOrder=''
	##
	# ParentFolderIds property
	#
	# @var EWSType_NonEmptyArrayOfBaseFolderIdsType
	#
	self.ParentFolderIds=''
	##
	# Traversal property
	#
	# @var EWSType_ItemQueryTraversalType
	#
	self.Traversal=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'ItemShape',
		'required' : True,
		'type' : 'ItemResponseShapeType',
		},
		{'name' : 'IndexedPageItemView',
		'required' : False,
		'type' : 'IndexedPageViewType',
		},
		{'name' : 'FractionalPageItemView',
		'required' : False,
		'type' : 'FractionalPageViewType',
		},
		{'name' : 'CalendarView',
		'required' : False,
		'type' : 'CalendarViewType',
		},
		{'name' : 'ContactsView',
		'required' : False,
		'type' : 'ContactsViewType',
		},
		{'name' : 'GroupBy',
		'required' : False,
		'type' : 'GroupByType',
		},
		{'name' : 'DistinguishedGroupBy',
		'required' : False,
		'type' : 'DistinguishedGroupByType',
		},
		{'name' : 'Restriction',
		'required' : False,
		'type' : 'RestrictionType',
		},
		{'name' : 'SortOrder',
		'required' : False,
		'type' : 'NonEmptyArrayOfFieldOrdersType',
		},
		{'name' : 'ParentFolderIds',
		'required' : False,
		'type' : 'NonEmptyArrayOfBaseFolderIdsType',
		},
		{'name' : 'Traversal',
		'required' : True,
		'type' : 'ItemQueryTraversalType',
		},
		]
# end this->schema
# end function __construct()
# end class FindItemType
