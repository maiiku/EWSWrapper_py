##
# Definition of the ConnectingSIDType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the ConnectingSIDType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_ConnectingSIDType (EWSType):
	##
	# PrincipalName property
	#
	# @var string
	#
	self.PrincipalName=''
	##
	# SID property
	#
	# @var string
	#
	self.SID=''
	##
	# PrimarySmtpAddress property
	#
	# @var string
	#
	self.PrimarySmtpAddress=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'PrincipalName',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'SID',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'PrimarySmtpAddress',
		'required' : False,
		'type' : 'string',
		},
		]
# end this->schema
# end function __construct()
# end class ConnectingSIDType
