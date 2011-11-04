##
# Definition of the FolderType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the FolderType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_FolderType (EWSType):
	##
	# PermissionSet property
	#
	# @var EWSType_PermissionSetType
	#
	self.PermissionSet=''
	##
	# UnreadCount property
	#
	# @var EWSType_int
	#
	self.UnreadCount=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'PermissionSet',
		'required' : False,
		'type' : 'PermissionSetType',
		},
		{'name' : 'UnreadCount',
		'required' : False,
		'type' : 'int',
		},
		]
# end this->schema
# end function __construct()
# end class FolderType
