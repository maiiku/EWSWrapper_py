##
# Definition of the FindItemParentType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the FindItemParentType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_FindItemParentType (EWSType):
	##
	# Items property
	#
	# @var EWSType_ArrayOfRealItemsType
	#
	self.Items=''
	##
	# Groups property
	#
	# @var EWSType_ArrayOfGroupedItemsType
	#
	self.Groups=''
	##
	# IndexedPagingOffset property
	#
	# @var EWSType_int
	#
	self.IndexedPagingOffset=''
	##
	# NumeratorOffset property
	#
	# @var EWSType_int
	#
	self.NumeratorOffset=''
	##
	# AbsoluteDenominator property
	#
	# @var EWSType_int
	#
	self.AbsoluteDenominator=''
	##
	# IncludesLastItemInRange property
	#
	# @var EWSType_boolean
	#
	self.IncludesLastItemInRange=''
	##
	# TotalItemsInView property
	#
	# @var EWSType_int
	#
	self.TotalItemsInView=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'Items',
		'required' : False,
		'type' : 'ArrayOfRealItemsType',
		},
		{'name' : 'Groups',
		'required' : False,
		'type' : 'ArrayOfGroupedItemsType',
		},
		{'name' : 'IndexedPagingOffset',
		'required' : False,
		'type' : 'int',
		},
		{'name' : 'NumeratorOffset',
		'required' : False,
		'type' : 'int',
		},
		{'name' : 'AbsoluteDenominator',
		'required' : False,
		'type' : 'int',
		},
		{'name' : 'IncludesLastItemInRange',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'TotalItemsInView',
		'required' : False,
		'type' : 'int',
		},
		]
# end this->schema
# end function __construct()
# end class FindItemParentType
