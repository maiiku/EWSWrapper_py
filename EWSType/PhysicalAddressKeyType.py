##
# Definition of the PhysicalAddressKeyType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Physical address key type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_PhysicalAddressKeyType (EWSType):
	##
	# Business physical address type
	#
	# @var string
	#
	self.BUSINESS='Business'
	##
	# Home physical address type
	#
	# @var string
	#
	self.HOME='Home'
	##
	# Other physical address type
	#
	# @var string
	#
	self.OTHER='Other'
	##
	# Value of the desired mapping. Should be one of the constants from the
	# EWSType_PhysicalAddressKeyType class.
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
# end class EWSType_PhysicalAddressKeyType
