##
# Definition of the BaseNotificationEventType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the BaseNotificationEventType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_BaseNotificationEventType (EWSType):
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
		self.schema = [{'name' : 'Watermark',
		'required' : False,
		'type' : 'WatermarkType',
		},
		]
# end this->schema
# end function __construct()
# end class BaseNotificationEventType
