##
# Definition of the FieldOrderType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the FieldOrderType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_FieldOrderType (EWSType):
	##
	# Path property
	#
	# @var EWSType_BasePathToElementType
	#
	self.Path=''
	##
	# Order property
	#
	# @var EWSType_SortDirectionType
	#
	self.Order=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'Path',
		'required' : False,
		'type' : 'BasePathToElementType',
		},
		{'name' : 'Order',
		'required' : True,
		'type' : 'SortDirectionType',
		},
		]
# end this->schema
# end function __construct()
# end class FieldOrderType
