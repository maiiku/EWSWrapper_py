##
# Definition of the UpdateFolderType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the UpdateFolderType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_UpdateFolderType (EWSType):
	##
	# FolderChanges property
	#
	# @var EWSType_NonEmptyArrayOfFolderChangesType
	#
	self.FolderChanges=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'FolderChanges',
		'required' : False,
		'type' : 'NonEmptyArrayOfFolderChangesType',
		},
		]
# end this->schema
# end function __construct()
# end class UpdateFolderType
