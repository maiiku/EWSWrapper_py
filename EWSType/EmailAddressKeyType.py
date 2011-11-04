##
# Definition of the EmailAddressKeyType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Email address key type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_EmailAddressKeyType (EWSType):
	##
	# Key for a contacts first email address
	#
	# @var string
	#
	self.EMAIL_ADDRESS_1='EmailAddress1'
	##
	# Key for a contacts second email address
	#
	# @var string
	#
	self.EMAIL_ADDRESS_2='EmailAddress2'
	##
	# Key for a contacts third email address
	#
	# @var string
	#
	self.EMAIL_ADDRESS_3='EmailAddress3'
	##
	# Value of the desired mapping. Should be one of the constants from the
	# EWSType_EmailAddressKeyType class.
	#
	# @var string
	#
	self._=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : '_',
		'required' : True,
		'type' : 'string',
		},
		]
# end this->schema
# end function __construct()
	##
	# Returns the value of this object as a string
	#
	# @return string
	#
	def __toString() :
		return self._
# end function __toString()
# end class EWSType_EmailAddressKeyType
