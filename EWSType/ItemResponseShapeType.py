##
# Definition of the ItemResponseShapeType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the ItemResponseShapeType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_ItemResponseShapeType (EWSType):
	##
	# BaseShape property
	#
	# @var EWSType_DefaultShapeNamesType
	#
	self.BaseShape=''
	##
	# IncludeMimeContent property
	#
	# @var EWSType_boolean
	#
	self.IncludeMimeContent=''
	##
	# BodyType property
	#
	# @var EWSType_BodyTypeResponseType
	#
	self.BodyType=''
	##
	# AdditionalProperties property
	#
	# @var EWSType_NonEmptyArrayOfPathsToElementType
	#
	self.AdditionalProperties=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'BaseShape',
		'required' : False,
		'type' : 'DefaultShapeNamesType',
		},
		{'name' : 'IncludeMimeContent',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'BodyType',
		'required' : False,
		'type' : 'BodyTypeResponseType',
		},
		{'name' : 'AdditionalProperties',
		'required' : False,
		'type' : 'NonEmptyArrayOfPathsToElementType',
		},
		]
# end this->schema
# end function __construct()
# end class ItemResponseShapeType
