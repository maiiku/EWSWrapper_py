##
# Definition of the FieldURIOrConstantType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the FieldURIOrConstantType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_FieldURIOrConstantType (EWSType):
	##
	# Path property
	#
	# @var EWSType_BasePathToElementType
	#
	self.Path=''
	##
	# Constant property
	#
	# @var EWSType_ConstantValueType
	#
	self.Constant=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'Path',
		'required' : False,
		'type' : 'BasePathToElementType',
		},
		{'name' : 'Constant',
		'required' : False,
		'type' : 'ConstantValueType',
		},
		]
# end this->schema
# end function __construct()
# end class FieldURIOrConstantType
