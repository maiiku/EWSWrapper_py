##
# Definition of the SetUserOofSettingsResponse type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the SetUserOofSettingsResponse type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_SetUserOofSettingsResponse (EWSType):
	##
	# ResponseMessage property
	#
	# @var EWSType_ResponseMessageType
	#
	self.ResponseMessage=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'ResponseMessage',
		'required' : False,
		'type' : 'ResponseMessageType',
		},
		]
# end this->schema
# end function __construct()
# end class SetUserOofSettingsResponse
