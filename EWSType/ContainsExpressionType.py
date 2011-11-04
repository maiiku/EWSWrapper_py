##
# Definition of the ContainsExpressionType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the ContainsExpressionType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_ContainsExpressionType (EWSType):
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
	# ContainmentMode property
	#
	# @var EWSType_ContainmentModeType
	#
	self.ContainmentMode=''
	##
	# ContainmentComparison property
	#
	# @var EWSType_ContainmentComparisonType
	#
	self.ContainmentComparison=''
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
		{'name' : 'ContainmentMode',
		'required' : False,
		'type' : 'ContainmentModeType',
		},
		{'name' : 'ContainmentComparison',
		'required' : False,
		'type' : 'ContainmentComparisonType',
		},
		]
# end this->schema
# end function __construct()
# end class ContainsExpressionType
