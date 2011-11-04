##
# Definition of the NonEmptyArrayOfFolderChangeDescriptionsType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the NonEmptyArrayOfFolderChangeDescriptionsType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_NonEmptyArrayOfFolderChangeDescriptionsType (EWSType):
	##
	# AppendToFolderField property
	#
	# @var EWSType_AppendToFolderFieldType
	#
	self.AppendToFolderField=''
	##
	# SetFolderField property
	#
	# @var EWSType_SetFolderFieldType
	#
	self.SetFolderField=''
	##
	# DeleteFolderField property
	#
	# @var EWSType_DeleteFolderFieldType
	#
	self.DeleteFolderField=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'AppendToFolderField',
		'required' : False,
		'type' : 'AppendToFolderFieldType',
		},
		{'name' : 'SetFolderField',
		'required' : False,
		'type' : 'SetFolderFieldType',
		},
		{'name' : 'DeleteFolderField',
		'required' : False,
		'type' : 'DeleteFolderFieldType',
		},
		]
# end this->schema
# end function __construct()
# end class NonEmptyArrayOfFolderChangeDescriptionsType
