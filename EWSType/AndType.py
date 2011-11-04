##
# Definition of the AndType type
#
# @author Michal Korzeniowski <mko_san@lafiel.net>
#
class EWSType_AndType (EWSType):
	##
	# SearchExpression property
	#
	# @var EWSType_MultipleOperandBooleanExpressionType
	#
	self.SearchExpression=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'SearchExpression',
		'required' : False,
		'type' : 'MultipleOperandBooleanExpressionType',
		},
		]
# end this->schema
# end function __construct()
# end class AndType
