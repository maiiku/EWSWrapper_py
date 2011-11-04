##
# Definition of the ContactsFolderType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the ContactsFolderType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_ContactsFolderType (EWSType):
	##
	# PermissionSet property
	#
	# @var EWSType_PermissionSetType
	#
	self.PermissionSet=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'PermissionSet',
		'required' : False,
		'type' : 'PermissionSetType',
		},
		]
# end this->schema
# end function __construct()
# end class ContactsFolderType
