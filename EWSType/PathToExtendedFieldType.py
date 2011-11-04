##
# Definition of the PathToExtendedFieldType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the PathToExtendedFieldType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_PathToExtendedFieldType (EWSType):
	##
	# DistinguishedPropertySetId property
	#
	# @var EWSType_DistinguishedPropertySetType
	#
	self.DistinguishedPropertySetId=''
	##
	# PropertySetId property
	#
	# @var EWSType_GuidType
	#
	self.PropertySetId=''
	##
	# PropertyTag property
	#
	# @var EWSType_PropertyTagType
	#
	self.PropertyTag=''
	##
	# PropertyName property
	#
	# @var string
	#
	self.PropertyName=''
	##
	# PropertyId property
	#
	# @var EWSType_int
	#
	self.PropertyId=''
	##
	# PropertyType property
	#
	# @var EWSType_MapiPropertyTypeType
	#
	self.PropertyType=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'DistinguishedPropertySetId',
		'required' : False,
		'type' : 'DistinguishedPropertySetType',
		},
		{'name' : 'PropertySetId',
		'required' : False,
		'type' : 'GuidType',
		},
		{'name' : 'PropertyTag',
		'required' : False,
		'type' : 'PropertyTagType',
		},
		{'name' : 'PropertyName',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'PropertyId',
		'required' : False,
		'type' : 'int',
		},
		{'name' : 'PropertyType',
		'required' : False,
		'type' : 'MapiPropertyTypeType',
		},
		]
# end this->schema
# end function __construct()
# end class PathToExtendedFieldType
