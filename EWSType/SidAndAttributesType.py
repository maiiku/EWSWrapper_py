##
# Definition of the SidAndAttributesType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the SidAndAttributesType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_SidAndAttributesType (EWSType):
	##
	# SecurityIdentifier property
	#
	# @var string
	#
	self.SecurityIdentifier=''
	##
	# Attributes property
	#
	# @var EWSType_unsignedInt
	#
	self.Attributes=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'SecurityIdentifier',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'Attributes',
		'required' : False,
		'type' : 'unsignedInt',
		},
		]
# end this->schema
# end function __construct()
# end class SidAndAttributesType
