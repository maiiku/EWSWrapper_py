##
# Definition of the TargetFolderIdType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the TargetFolderIdType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_TargetFolderIdType (EWSType):
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
		]
# end this->schema
# end function __construct()
# end class TargetFolderIdType
