##
# Definition of the DeleteFolderType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the DeleteFolderType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_DeleteFolderType (EWSType):
	##
	# FolderIds property
	#
	# @var EWSType_NonEmptyArrayOfBaseFolderIdsType
	#
	self.FolderIds=''
	##
	# DeleteType property
	#
	# @var EWSType_DisposalType
	#
	self.DeleteType=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'FolderIds',
		'required' : False,
		'type' : 'NonEmptyArrayOfBaseFolderIdsType',
		},
		{'name' : 'DeleteType',
		'required' : False,
		'type' : 'DisposalType',
		},
		]
# end this->schema
# end function __construct()
# end class DeleteFolderType
