##
# Definition of the IndexedPageViewType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the IndexedPageViewType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_IndexedPageViewType (EWSType):
	##
	# Offset property
	#
	# @var EWSType_int
	#
	self.Offset=''
	##
	# BasePoint property
	#
	# @var EWSType_IndexBasePointType
	#
	self.BasePoint=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'Offset',
		'required' : False,
		'type' : 'int',
		},
		{'name' : 'BasePoint',
		'required' : False,
		'type' : 'IndexBasePointType',
		},
		]
# end this->schema
# end function __construct()
# end class IndexedPageViewType
