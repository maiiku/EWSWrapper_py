##
# Definition of the SendNotificationResultType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the SendNotificationResultType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_SendNotificationResultType (EWSType):
	##
	# SubscriptionStatus property
	#
	# @var EWSType_SubscriptionStatusType
	#
	self.SubscriptionStatus=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'SubscriptionStatus',
		'required' : False,
		'type' : 'SubscriptionStatusType',
		},
		]
# end this->schema
# end function __construct()
# end class SendNotificationResultType
