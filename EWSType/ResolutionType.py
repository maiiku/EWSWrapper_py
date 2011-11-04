##
# Definition of the ResolutionType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the ResolutionType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_ResolutionType (EWSType):
	##
	# Mailbox property
	#
	# @var EWSType_EmailAddressType
	#
	self.Mailbox=''
	##
	# Contact property
	#
	# @var EWSType_ContactItemType
	#
	self.Contact=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'Mailbox',
		'required' : False,
		'type' : 'EmailAddressType',
		},
		{'name' : 'Contact',
		'required' : False,
		'type' : 'ContactItemType',
		},
		]
# end this->schema
# end function __construct()
# end class ResolutionType
