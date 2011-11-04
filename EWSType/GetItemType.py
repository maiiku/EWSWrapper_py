##
# Definition of the GetItemType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the GetItemType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_GetItemType (EWSType):
	##
	# ItemShape property
	#
	# @var EWSType_ItemResponseShapeType
	#
	self.ItemShape=''
	##
	# ItemIds property
	#
	# @var EWSType_NonEmptyArrayOfBaseItemIdsType
	#
	self.ItemIds=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'ItemShape',
		'required' : False,
		'type' : 'ItemResponseShapeType',
		},
		{'name' : 'ItemIds',
		'required' : False,
		'type' : 'NonEmptyArrayOfBaseItemIdsType',
		},
		]
# end this->schema
# end function __construct()
# end class GetItemType
