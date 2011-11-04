##
# Definition of the GetUserOofSettingsResponse type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the GetUserOofSettingsResponse type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_GetUserOofSettingsResponse (EWSType):
	##
	# ResponseMessage property
	#
	# @var EWSType_ResponseMessageType
	#
	self.ResponseMessage=''
	##
	# OofSettings property
	#
	# @var EWSType_UserOofSettings
	#
	self.OofSettings=''
	##
	# AllowExternalOof property
	#
	# @var EWSType_ExternalAudience
	#
	self.AllowExternalOof=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'ResponseMessage',
		'required' : False,
		'type' : 'ResponseMessageType',
		},
		{'name' : 'OofSettings',
		'required' : False,
		'type' : 'UserOofSettings',
		},
		{'name' : 'AllowExternalOof',
		'required' : False,
		'type' : 'ExternalAudience',
		},
		]
# end this->schema
# end function __construct()
# end class GetUserOofSettingsResponse
