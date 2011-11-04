##
# Definition of the NonEmptyArrayOfItemChangesType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the NonEmptyArrayOfItemChangesType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_NonEmptyArrayOfItemChangesType (EWSType):
	##
	# ItemChange property
	#
	# @var EWSType_ItemChangeType
	#
	self.ItemChange=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'ItemChange',
		'required' : False,
		'type' : 'ItemChangeType',
		},
		]
# end this->schema
# end function __construct()
# end class NonEmptyArrayOfItemChangesType
