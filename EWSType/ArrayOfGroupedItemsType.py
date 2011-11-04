##
# Definition of the ArrayOfGroupedItemsType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the ArrayOfGroupedItemsType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_ArrayOfGroupedItemsType (EWSType):
	##
	# GroupedItems property
	#
	# @var EWSType_GroupedItemsType
	#
	self.GroupedItems=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'GroupedItems',
		'required' : False,
		'type' : 'GroupedItemsType',
		},
		]
# end this->schema
# end function __construct()
# end class ArrayOfGroupedItemsType
