##
# Definition of the RestrictionType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_RestrictionType (EWSType):
	##
	# SearchExpression property
	#
	# @var EWSType_SearchExpressionType
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
# end class RestrictionType
