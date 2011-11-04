##
# Definition of the Value type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the Value type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_Value (EWSType):
	##
	# _ property
	#
	# @var string
	#
	self._=''
	##
	# Name property
	#
	# @var string
	#
	self.Name=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : '_',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'Name',
		'required' : False,
		'type' : 'string',
		},
		]
# end this->schema
# end function __construct()
# end class Value
