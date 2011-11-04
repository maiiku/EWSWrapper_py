##
# Definition of the AlternateIdType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the AlternateIdType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_AlternateIdType (EWSType):
	##
	# Id property
	#
	# @var string
	#
	self.Id=''
	##
	# Mailbox property
	#
	# @var EWSType_NonEmptyStringType
	#
	self.Mailbox=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'Id',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'Mailbox',
		'required' : False,
		'type' : 'NonEmptyStringType',
		},
		]
# end this->schema
# end function __construct()
# end class AlternateIdType
