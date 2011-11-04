##
# Definition of the SerializedSecurityContextType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the SerializedSecurityContextType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_SerializedSecurityContextType (EWSType):
	##
	# UserSid property
	#
	# @var string
	#
	self.UserSid=''
	##
	# GroupSids property
	#
	# @var EWSType_NonEmptyArrayOfGroupIdentifiersType
	#
	self.GroupSids=''
	##
	# RestrictedGroupSids property
	#
	# @var EWSType_NonEmptyArrayOfRestrictedGroupIdentifiersType
	#
	self.RestrictedGroupSids=''
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
		self.schema = [{'name' : 'UserSid',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'GroupSids',
		'required' : False,
		'type' : 'NonEmptyArrayOfGroupIdentifiersType',
		},
		{'name' : 'RestrictedGroupSids',
		'required' : False,
		'type' : 'NonEmptyArrayOfRestrictedGroupIdentifiersType',
		},
		{'name' : 'PrimarySmtpAddress',
		'required' : False,
		'type' : 'string',
		},
		]
# end this->schema
# end function __construct()
# end class SerializedSecurityContextType
