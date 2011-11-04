##
# Definition of the UserIdType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the UserIdType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_UserIdType (EWSType):
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
	# DisplayName property
	#
	# @var string
	#
	self.DisplayName=''
	##
	# DistinguishedUser property
	#
	# @var EWSType_DistinguishedUserType
	#
	self.DistinguishedUser=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'SID',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'PrimarySmtpAddress',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'DisplayName',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'DistinguishedUser',
		'required' : False,
		'type' : 'DistinguishedUserType',
		},
		]
# end this->schema
# end function __construct()
# end class UserIdType
