##
# Definition of the CreateFolderType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the CreateFolderType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_CreateFolderType (EWSType):
	##
	# ParentFolderId property
	#
	# @var EWSType_TargetFolderIdType
	#
	self.ParentFolderId=''
	##
	# Folders property
	#
	# @var EWSType_NonEmptyArrayOfFoldersType
	#
	self.Folders=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'ParentFolderId',
		'required' : False,
		'type' : 'TargetFolderIdType',
		},
		{'name' : 'Folders',
		'required' : False,
		'type' : 'NonEmptyArrayOfFoldersType',
		},
		]
# end this->schema
# end function __construct()
# end class CreateFolderType
