##
# Definition of the SetUserOofSettingsRequest type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the SetUserOofSettingsRequest type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_SetUserOofSettingsRequest (EWSType):
	##
	# Mailbox property
	#
	# @var EWSType_EmailAddress
	#
	self.Mailbox=''
	##
	# UserOofSettings property
	#
	# @var EWSType_UserOofSettings
	#
	self.UserOofSettings=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'Mailbox',
		'required' : False,
		'type' : 'EmailAddress',
		},
		{'name' : 'UserOofSettings',
		'required' : False,
		'type' : 'UserOofSettings',
		},
		]
# end this->schema
# end function __construct()
# end class SetUserOofSettingsRequest
