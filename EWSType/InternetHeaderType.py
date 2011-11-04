##
# Definition of the InternetHeaderType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the InternetHeaderType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_InternetHeaderType (EWSType):
	##
	# _ property
	#
	# @var string
	#
	self._=''
	##
	# HeaderName property
	#
	# @var string
	#
	self.HeaderName=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : '_',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'HeaderName',
		'required' : False,
		'type' : 'string',
		},
		]
# end this->schema
# end function __construct()
# end class InternetHeaderType
