##
# Definition of the CreateManagedFolderRequestType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the CreateManagedFolderRequestType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_CreateManagedFolderRequestType (EWSType):
	##
	# FolderNames property
	#
	# @var EWSType_NonEmptyArrayOfFolderNamesType
	#
	self.FolderNames=''
	##
	# Mailbox property
	#
	# @var EWSType_EmailAddressType
	#
	self.Mailbox=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'FolderNames',
		'required' : False,
		'type' : 'NonEmptyArrayOfFolderNamesType',
		},
		{'name' : 'Mailbox',
		'required' : False,
		'type' : 'EmailAddressType',
		},
		]
# end this->schema
# end function __construct()
# end class CreateManagedFolderRequestType
