##
# Definition of the GetEventsResponseMessageType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the GetEventsResponseMessageType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_GetEventsResponseMessageType (EWSType):
	##
	# Notification property
	#
	# @var EWSType_NotificationType
	#
	self.Notification=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'Notification',
		'required' : False,
		'type' : 'NotificationType',
		},
		]
# end this->schema
# end function __construct()
# end class GetEventsResponseMessageType
