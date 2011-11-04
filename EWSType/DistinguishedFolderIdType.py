##
# Definition of the DistinguishedFolderIdType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the DistinguishedFolderIdType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_DistinguishedFolderIdType (EWSType):
	##
	# Mailbox property
	#
	# @var EWSType_EmailAddressType
	#
	self.Mailbox=''
	##
	# Id property
	#
	# @var EWSType_DistinguishedFolderIdNameType
	#
	self.Id=''
	##
	# ChangeKey property
	#
	# @var string
	#
	self.ChangeKey=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'Mailbox',
		'required' : False,
		'type' : 'EmailAddressType',
		},
		{'name' : 'Id',
		'required' : False,
		'type' : 'DistinguishedFolderIdNameType',
		},
		{'name' : 'ChangeKey',
		'required' : False,
		'type' : 'string',
		},
		]
# end this->schema
# end function __construct()
# end class DistinguishedFolderIdType
