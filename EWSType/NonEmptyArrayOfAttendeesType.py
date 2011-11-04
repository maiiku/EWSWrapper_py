##
# Definition of the NonEmptyArrayOfSearchExpressionType type
#
# @author Michal Korzeniowski <mko_san@lafiel.net>
#
class EWSType_NonEmptyArrayOfSearchExpressionType (EWSType):
	##
	# Attendee property
	#
	# @var EWSType_RestrictionType
	#
	self.SearchExpression=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'SearchExpression',
		'required' : False,
		'type' : 'SearchExpressionType',
		},
		]
# end this->schema
# end function __construct()
# end class NonEmptyArrayOfSearchExpressionType
