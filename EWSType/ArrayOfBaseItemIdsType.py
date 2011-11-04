##
# Definition of the ArrayOfBaseItemIdsType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the ArrayOfBaseItemIdsType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_ArrayOfBaseItemIdsType (EWSType):
	##
	# ItemId property
	#
	# @var EWSType_ItemIdType
	#
	self.ItemId=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'ItemId',
		'required' : False,
		'type' : 'ItemIdType',
		},
		]
# end this->schema
# end function __construct()
# end class ArrayOfBaseItemIdsType
