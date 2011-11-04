##
# Definition of the NonEmptyArrayOfGroupIdentifiersType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the NonEmptyArrayOfGroupIdentifiersType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_NonEmptyArrayOfGroupIdentifiersType (EWSType):
	##
	# GroupIdentifier property
	#
	# @var EWSType_SidAndAttributesType
	#
	self.GroupIdentifier=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'GroupIdentifier',
		'required' : False,
		'type' : 'SidAndAttributesType',
		},
		]
# end this->schema
# end function __construct()
# end class NonEmptyArrayOfGroupIdentifiersType
