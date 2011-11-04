##
# Definition of the PhoneNumberDictionaryEntryType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the PhoneNumberDictionaryEntryType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_PhoneNumberDictionaryEntryType (EWSType):
	##
	# _ property
	#
	# @var string
	#
	self._=''
	##
	# Key property
	#
	# @var EWSType_PhoneNumberKeyType
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
		'type' : 'PhoneNumberKeyType',
		},
		]
# end this->schema
# end function __construct()
# end class PhoneNumberDictionaryEntryType
