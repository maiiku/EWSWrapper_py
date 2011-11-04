##
# Definition of the PhysicalAddressDictionaryEntryType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the PhysicalAddressDictionaryEntryType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_PhysicalAddressDictionaryEntryType (EWSType):
	##
	# Street property
	#
	# @var string
	#
	self.Street=''
	##
	# City property
	#
	# @var string
	#
	self.City=''
	##
	# State property
	#
	# @var string
	#
	self.State=''
	##
	# CountryOrRegion property
	#
	# @var string
	#
	self.CountryOrRegion=''
	##
	# PostalCode property
	#
	# @var string
	#
	self.PostalCode=''
	##
	# Key property
	#
	# @var EWSType_PhysicalAddressKeyType
	#
	self.Key=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'Street',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'City',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'State',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'CountryOrRegion',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'PostalCode',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'Key',
		'required' : False,
		'type' : 'PhysicalAddressKeyType',
		},
		]
# end this->schema
# end function __construct()
# end class PhysicalAddressDictionaryEntryType
