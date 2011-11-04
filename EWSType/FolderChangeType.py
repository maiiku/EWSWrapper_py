##
# Definition of the FolderChangeType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the FolderChangeType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_FolderChangeType (EWSType):
	##
	# FolderId property
	#
	# @var EWSType_FolderIdType
	#
	self.FolderId=''
	##
	# DistinguishedFolderId property
	#
	# @var EWSType_DistinguishedFolderIdType
	#
	self.DistinguishedFolderId=''
	##
	# Updates property
	#
	# @var EWSType_NonEmptyArrayOfFolderChangeDescriptionsType
	#
	self.Updates=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'FolderId',
		'required' : False,
		'type' : 'FolderIdType',
		},
		{'name' : 'DistinguishedFolderId',
		'required' : False,
		'type' : 'DistinguishedFolderIdType',
		},
		{'name' : 'Updates',
		'required' : False,
		'type' : 'NonEmptyArrayOfFolderChangeDescriptionsType',
		},
		]
# end this->schema
# end function __construct()
# end class FolderChangeType
