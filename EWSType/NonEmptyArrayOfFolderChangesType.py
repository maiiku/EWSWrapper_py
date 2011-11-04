##
# Definition of the NonEmptyArrayOfFolderChangesType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the NonEmptyArrayOfFolderChangesType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_NonEmptyArrayOfFolderChangesType (EWSType):
	##
	# FolderChange property
	#
	# @var EWSType_FolderChangeType
	#
	self.FolderChange=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'FolderChange',
		'required' : False,
		'type' : 'FolderChangeType',
		},
		]
# end this->schema
# end function __construct()
# end class NonEmptyArrayOfFolderChangesType
