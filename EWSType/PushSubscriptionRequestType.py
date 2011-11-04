##
# Definition of the PushSubscriptionRequestType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the PushSubscriptionRequestType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_PushSubscriptionRequestType (EWSType):
	##
	# StatusFrequency property
	#
	# @var EWSType_SubscriptionStatusFrequencyType
	#
	self.StatusFrequency=''
	##
	# URL property
	#
	# @var string
	#
	self.URL=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'StatusFrequency',
		'required' : False,
		'type' : 'SubscriptionStatusFrequencyType',
		},
		{'name' : 'URL',
		'required' : False,
		'type' : 'string',
		},
		]
# end this->schema
# end function __construct()
# end class PushSubscriptionRequestType
