##
# Definition of the EmailAddress type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the EmailAddress type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_EmailAddress (EWSType):
	##
	# Name property
	#
	# @var string
	#
	self.Name=''
	##
	# Address property
	#
	# @var string
	#
	self.Address=''
	##
	# RoutingType property
	#
	# @var string
	#
	self.RoutingType=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'Name',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'Address',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'RoutingType',
		'required' : False,
		'type' : 'string',
		},
		]
# end this->schema
# end function __construct()
# end class EmailAddress
