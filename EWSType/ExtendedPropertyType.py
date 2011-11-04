##
# Definition of the ExtendedPropertyType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the ExtendedPropertyType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_ExtendedPropertyType (EWSType):
	##
	# ExtendedFieldURI property
	#
	# @var EWSType_PathToExtendedFieldType
	#
	self.ExtendedFieldURI=''
	##
	# Value property
	#
	# @var string
	#
	self.Value=''
	##
	# Values property
	#
	# @var EWSType_NonEmptyArrayOfPropertyValuesType
	#
	self.Values=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'ExtendedFieldURI',
		'required' : False,
		'type' : 'PathToExtendedFieldType',
		},
		{'name' : 'Value',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'Values',
		'required' : False,
		'type' : 'NonEmptyArrayOfPropertyValuesType',
		},
		]
# end this->schema
# end function __construct()
# end class ExtendedPropertyType
