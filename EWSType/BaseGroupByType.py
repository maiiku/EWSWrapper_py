##
# Definition of the BaseGroupByType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the BaseGroupByType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_BaseGroupByType (EWSType):
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
		self.schema = [{'name' : 'Order',
		'required' : False,
		'type' : 'SortDirectionType',
		},
		]
# end this->schema
# end function __construct()
# end class BaseGroupByType
