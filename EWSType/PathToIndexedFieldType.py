##
# Definition of the PathToIndexedFieldType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the PathToIndexedFieldType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_PathToIndexedFieldType (EWSType):
	##
	# FieldURI property
	#
	# @var EWSType_DictionaryURIType
	#
	self.FieldURI=''
	##
	# FieldIndex property
	#
	# @var string
	#
	self.FieldIndex=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'FieldURI',
		'required' : False,
		'type' : 'DictionaryURIType',
		},
		{'name' : 'FieldIndex',
		'required' : False,
		'type' : 'string',
		},
		]
# end this->schema
# end function __construct()
# end class PathToIndexedFieldType
