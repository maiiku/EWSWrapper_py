##
# Definition of the TwoOperandExpressionType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_TwoOperandExpressionType (EWSType):
	##
	# Path property
	#
	# @var EWSType_BasePathToElementType
	#
	self.Path=''
	##
	# FieldURIOrConstant property
	#
	# @var EWSType_FieldURIOrConstantType
	#
	self.FieldURIOrConstant=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'Path',
		'required' : False,
		'type' : 'BasePathToElementType',
		},
		{'name' : 'FieldURIOrConstant',
		'required' : False,
		'type' : 'FieldURIOrConstantType',
		},
		]
# end this->schema
# end function __construct()
# end class TwoOperandExpressionType
