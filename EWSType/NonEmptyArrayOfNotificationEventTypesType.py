##
# Definition of the NonEmptyArrayOfNotificationEventTypesType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the NonEmptyArrayOfNotificationEventTypesType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_NonEmptyArrayOfNotificationEventTypesType (EWSType):
	##
	# EventType property
	#
	# @var EWSType_NotificationEventTypeType
	#
	self.EventType=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'EventType',
		'required' : False,
		'type' : 'NotificationEventTypeType',
		},
		]
# end this->schema
# end function __construct()
# end class NonEmptyArrayOfNotificationEventTypesType
