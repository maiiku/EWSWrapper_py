##
# Definition of the BasePagingType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the BasePagingType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_BasePagingType (EWSType):
	##
	# MaxEntriesReturned property
	#
	# @var EWSType_int
	#
	self.MaxEntriesReturned=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'MaxEntriesReturned',
		'required' : False,
		'type' : 'int',
		},
		]
# end this->schema
# end function __construct()
# end class BasePagingType
