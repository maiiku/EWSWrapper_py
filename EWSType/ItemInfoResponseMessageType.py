##
# Definition of the ItemInfoResponseMessageType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the ItemInfoResponseMessageType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_ItemInfoResponseMessageType (EWSType):
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
		self.schema = [{'name' : 'Items',
		'required' : False,
		'type' : 'ArrayOfRealItemsType',
		},
		]
# end this->schema
# end function __construct()
# end class ItemInfoResponseMessageType
