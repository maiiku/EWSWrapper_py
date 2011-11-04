##
# Definition of the EmailAddressDictionaryEntryType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the EmailAddressDictionaryEntryType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_EmailAddressDictionaryEntryType (EWSType):
	##
	# _ property
	#
	# @var string
	#
	self._=''
	##
	# Key property
	#
	# @var EWSType_EmailAddressKeyType
	#
	self.Key=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : '_',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'Key',
		'required' : False,
		'type' : 'EmailAddressKeyType',
		},
		]
# end this->schema
# end function __construct()
# end class EmailAddressDictionaryEntryType
