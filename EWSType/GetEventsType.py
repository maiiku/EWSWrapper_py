##
# Definition of the GetEventsType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the GetEventsType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_GetEventsType (EWSType):
	##
	# SubscriptionId property
	#
	# @var EWSType_SubscriptionIdType
	#
	self.SubscriptionId=''
	##
	# Watermark property
	#
	# @var EWSType_WatermarkType
	#
	self.Watermark=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'SubscriptionId',
		'required' : False,
		'type' : 'SubscriptionIdType',
		},
		{'name' : 'Watermark',
		'required' : False,
		'type' : 'WatermarkType',
		},
		]
# end this->schema
# end function __construct()
# end class GetEventsType
