##
# Definition of the ExpandDLType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the ExpandDLType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_ExpandDLType (EWSType):
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
		self.schema = [{'name' : 'Mailbox',
		'required' : False,
		'type' : 'EmailAddressType',
		},
		]
# end this->schema
# end function __construct()
# end class ExpandDLType
