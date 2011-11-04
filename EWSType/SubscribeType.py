##
# Definition of the SubscribeType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the SubscribeType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_SubscribeType (EWSType):
	##
	# PullSubscriptionRequest property
	#
	# @var EWSType_PullSubscriptionRequestType
	#
	self.PullSubscriptionRequest=''
	##
	# PushSubscriptionRequest property
	#
	# @var EWSType_PushSubscriptionRequestType
	#
	self.PushSubscriptionRequest=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'PullSubscriptionRequest',
		'required' : False,
		'type' : 'PullSubscriptionRequestType',
		},
		{'name' : 'PushSubscriptionRequest',
		'required' : False,
		'type' : 'PushSubscriptionRequestType',
		},
		]
# end this->schema
# end function __construct()
# end class SubscribeType
