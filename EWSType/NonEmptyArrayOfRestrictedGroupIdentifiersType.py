##
# Definition of the NonEmptyArrayOfRestrictedGroupIdentifiersType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the NonEmptyArrayOfRestrictedGroupIdentifiersType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_NonEmptyArrayOfRestrictedGroupIdentifiersType (EWSType):
	##
	# RestrictedGroupIdentifier property
	#
	# @var EWSType_SidAndAttributesType
	#
	self.RestrictedGroupIdentifier=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'RestrictedGroupIdentifier',
		'required' : False,
		'type' : 'SidAndAttributesType',
		},
		]
# end this->schema
# end function __construct()
# end class NonEmptyArrayOfRestrictedGroupIdentifiersType
