##
# Definition of the ArrayOfMailboxData type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the ArrayOfMailboxData type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_ArrayOfMailboxData (EWSType):
	##
	# MailboxData property
	#
	# @var EWSType_MailboxData
	#
	self.MailboxData=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'MailboxData',
		'required' : False,
		'type' : 'MailboxData',
		},
		]
# end this->schema
# end function __construct()
# end class ArrayOfMailboxData
