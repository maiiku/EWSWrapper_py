##
# Definition of the BaseSubscriptionRequestType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the BaseSubscriptionRequestType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_BaseSubscriptionRequestType (EWSType):
	##
	# FolderIds property
	#
	# @var EWSType_NonEmptyArrayOfBaseFolderIdsType
	#
	self.FolderIds=''
	##
	# EventTypes property
	#
	# @var EWSType_NonEmptyArrayOfNotificationEventTypesType
	#
	self.EventTypes=''
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
		self.schema = [{'name' : 'FolderIds',
		'required' : False,
		'type' : 'NonEmptyArrayOfBaseFolderIdsType',
		},
		{'name' : 'EventTypes',
		'required' : False,
		'type' : 'NonEmptyArrayOfNotificationEventTypesType',
		},
		{'name' : 'Watermark',
		'required' : False,
		'type' : 'WatermarkType',
		},
		]
# end this->schema
# end function __construct()
# end class BaseSubscriptionRequestType
