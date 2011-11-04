##
# Definition of the FolderResponseShapeType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the FolderResponseShapeType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_FolderResponseShapeType (EWSType):
	##
	# BaseShape property
	#
	# @var EWSType_DefaultShapeNamesType
	#
	self.BaseShape=''
	##
	# AdditionalProperties property
	#
	# @var EWSType_NonEmptyArrayOfPathsToElementType
	#
	self.AdditionalProperties=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'BaseShape',
		'required' : False,
		'type' : 'DefaultShapeNamesType',
		},
		{'name' : 'AdditionalProperties',
		'required' : False,
		'type' : 'NonEmptyArrayOfPathsToElementType',
		},
		]
# end this->schema
# end function __construct()
# end class FolderResponseShapeType
