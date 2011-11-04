##
# Definition of the AttendeeType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the AttendeeType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_AttendeeType (EWSType):
	##
	# Mailbox property
	#
	# @var EWSType_EmailAddressType
	#
	self.Mailbox=''
	##
	# ResponseType property
	#
	# @var EWSType_ResponseTypeType
	#
	self.ResponseType=''
	##
	# LastResponseTime property
	#
	# @var EWSType_dateTime
	#
	self.LastResponseTime=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'Mailbox',
		'required' : False,
		'type' : 'EmailAddressType',
		},
		{'name' : 'ResponseType',
		'required' : False,
		'type' : 'ResponseTypeType',
		},
		{'name' : 'LastResponseTime',
		'required' : False,
		'type' : 'dateTime',
		},
		]
# end this->schema
# end function __construct()
# end class AttendeeType
