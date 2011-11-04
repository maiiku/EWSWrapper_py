##
# Definition of the NonEmptyArrayOfAlternateIdsType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the NonEmptyArrayOfAlternateIdsType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_NonEmptyArrayOfAlternateIdsType (EWSType):
	##
	# AlternateId property
	#
	# @var EWSType_AlternateIdType
	#
	self.AlternateId=''
	##
	# AlternatePublicFolderId property
	#
	# @var EWSType_AlternatePublicFolderIdType
	#
	self.AlternatePublicFolderId=''
	##
	# AlternatePublicFolderItemId property
	#
	# @var EWSType_AlternatePublicFolderItemIdType
	#
	self.AlternatePublicFolderItemId=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'AlternateId',
		'required' : False,
		'type' : 'AlternateIdType',
		},
		{'name' : 'AlternatePublicFolderId',
		'required' : False,
		'type' : 'AlternatePublicFolderIdType',
		},
		{'name' : 'AlternatePublicFolderItemId',
		'required' : False,
		'type' : 'AlternatePublicFolderItemIdType',
		},
		]
# end this->schema
# end function __construct()
# end class NonEmptyArrayOfAlternateIdsType
