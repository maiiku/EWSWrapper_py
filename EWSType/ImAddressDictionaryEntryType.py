##
# Definition of the ImAddressDictionaryEntryType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the ImAddressDictionaryEntryType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_ImAddressDictionaryEntryType (EWSType):
	##
	# _ property
	#
	# @var string
	#
	self._=''
	##
	# Key property
	#
	# @var EWSType_ImAddressKeyType
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
		'type' : 'ImAddressKeyType',
		},
		]
# end this->schema
# end function __construct()
# end class ImAddressDictionaryEntryType
