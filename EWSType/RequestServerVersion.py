##
# Definition of the RequestServerVersion type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the RequestServerVersion type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_RequestServerVersion (EWSType):
	##
	# Version property
	#
	# @var EWSType_ExchangeVersionType
	#
	self.Version=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'Version',
		'required' : False,
		'type' : 'ExchangeVersionType',
		},
		]
# end this->schema
# end function __construct()
# end class RequestServerVersion
