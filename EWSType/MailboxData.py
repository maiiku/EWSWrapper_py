##
# Definition of the MailboxData type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the MailboxData type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_MailboxData (EWSType):
	##
	# Email property
	#
	# @var EWSType_EmailAddress
	#
	self.Email=''
	##
	# AttendeeType property
	#
	# @var EWSType_MeetingAttendeeType
	#
	self.AttendeeType=''
	##
	# ExcludeConflicts property
	#
	# @var EWSType_boolean
	#
	self.ExcludeConflicts=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'Email',
		'required' : False,
		'type' : 'EmailAddress',
		},
		{'name' : 'AttendeeType',
		'required' : False,
		'type' : 'MeetingAttendeeType',
		},
		{'name' : 'ExcludeConflicts',
		'required' : False,
		'type' : 'boolean',
		},
		]
# end this->schema
# end function __construct()
# end class MailboxData
