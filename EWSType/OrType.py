##
# Definition of the IsGreaterThanOrEqualToType type
#
# @author Michal Korzeniowski <mko_san@lafiel.net>
#
class EWSType_OrType (EWSType):
	##
	# SearchExpression property
	#
	# @var EWSType_IsGreaterThanOrEqualToType
	#
	self.SearchExpression=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'SearchExpression',
		'required' : False,
		'type' : 'IsGreaterThanOrEqualToType',
		},
		]
# end this->schema
# end function __construct()
# end class IsGreaterThanOrEqualToType
