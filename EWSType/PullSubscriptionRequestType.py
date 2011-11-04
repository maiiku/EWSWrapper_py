##
# Definition of the PullSubscriptionRequestType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the PullSubscriptionRequestType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_PullSubscriptionRequestType (EWSType):
	##
	# Timeout property
	#
	# @var EWSType_SubscriptionTimeoutType
	#
	self.Timeout=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'Timeout',
		'required' : False,
		'type' : 'SubscriptionTimeoutType',
		},
		]
# end this->schema
# end function __construct()
# end class PullSubscriptionRequestType
