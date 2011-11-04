##
# Definition of the GetUserOofSettingsRequest type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the GetUserOofSettingsRequest type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_GetUserOofSettingsRequest (EWSType):
	##
	# Mailbox property
	#
	# @var EWSType_EmailAddress
	#
	self.Mailbox=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'Mailbox',
		'required' : False,
		'type' : 'EmailAddress',
		},
		]
# end this->schema
# end function __construct()
# end class GetUserOofSettingsRequest
