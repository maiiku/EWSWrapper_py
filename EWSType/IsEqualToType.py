##
# Definition of the IsEqualToType type
#
# @author Michal Korzeniowski <mko_san@lafiel.net>
#
class EWSType_IsEqualToType (EWSType):
	##
	# SearchExpression property
	#
	# @var EWSType_TwoOperandExpressionType
	#
	self.SearchExpression=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'SearchExpression',
		'required' : False,
		'type' : 'TwoOperandExpressionType',
		},
		]
# end this->schema
# end function __construct()
# end class IsEqualToType
