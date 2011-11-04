##
# Definition of the GroupedItemsType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the GroupedItemsType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_GroupedItemsType (EWSType):
	##
	# GroupIndex property
	#
	# @var string
	#
	self.GroupIndex=''
	##
	# Items property
	#
	# @var EWSType_ArrayOfRealItemsType
	#
	self.Items=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'GroupIndex',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'Items',
		'required' : False,
		'type' : 'ArrayOfRealItemsType',
		},
		]
# end this->schema
# end function __construct()
# end class GroupedItemsType
