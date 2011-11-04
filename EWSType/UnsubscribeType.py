##
# Definition of the UnsubscribeType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the UnsubscribeType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_UnsubscribeType (EWSType):
	##
	# SubscriptionId property
	#
	# @var EWSType_SubscriptionIdType
	#
	self.SubscriptionId=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'SubscriptionId',
		'required' : False,
		'type' : 'SubscriptionIdType',
		},
		]
# end this->schema
# end function __construct()
# end class UnsubscribeType
