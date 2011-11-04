##
# Definition of the NonEmptyArrayOfItemChangeDescriptionsType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the NonEmptyArrayOfItemChangeDescriptionsType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_NonEmptyArrayOfItemChangeDescriptionsType (EWSType):
	##
	# AppendToItemField property
	#
	# @var EWSType_AppendToItemFieldType
	#
	self.AppendToItemField=''
	##
	# SetItemField property
	#
	# @var EWSType_SetItemFieldType
	#
	self.SetItemField=''
	##
	# DeleteItemField property
	#
	# @var EWSType_DeleteItemFieldType
	#
	self.DeleteItemField=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'AppendToItemField',
		'required' : False,
		'type' : 'AppendToItemFieldType',
		},
		{'name' : 'SetItemField',
		'required' : False,
		'type' : 'SetItemFieldType',
		},
		{'name' : 'DeleteItemField',
		'required' : False,
		'type' : 'DeleteItemFieldType',
		},
		]
# end this->schema
# end function __construct()
# end class NonEmptyArrayOfItemChangeDescriptionsType
