##
# Definition of the ArrayOfUnknownEntriesType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the ArrayOfUnknownEntriesType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_ArrayOfUnknownEntriesType (EWSType):
	##
	# UnknownEntry property
	#
	# @var string
	#
	self.UnknownEntry=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'UnknownEntry',
		'required' : False,
		'type' : 'string',
		},
		]
# end this->schema
# end function __construct()
# end class ArrayOfUnknownEntriesType
