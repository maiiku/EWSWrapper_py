##
# Definition of the EmailAddressType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the EmailAddressType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_EmailAddressType (EWSType):
	##
	# Name property
	#
	# @var string
	#
	self.Name=''
	##
	# EmailAddress property
	#
	# @var EWSType_NonEmptyStringType
	#
	self.EmailAddress=''
	##
	# RoutingType property
	#
	# @var EWSType_NonEmptyStringType
	#
	self.RoutingType=''
	##
	# MailboxType property
	#
	# @var EWSType_MailboxTypeType
	#
	self.MailboxType=''
	##
	# ItemId property
	#
	# @var EWSType_ItemIdType
	#
	self.ItemId=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'Name',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'EmailAddress',
		'required' : False,
		'type' : 'NonEmptyStringType',
		},
		{'name' : 'RoutingType',
		'required' : False,
		'type' : 'NonEmptyStringType',
		},
		{'name' : 'MailboxType',
		'required' : False,
		'type' : 'MailboxTypeType',
		},
		{'name' : 'ItemId',
		'required' : False,
		'type' : 'ItemIdType',
		},
		]
# end this->schema
# end function __construct()
# end class EmailAddressType
