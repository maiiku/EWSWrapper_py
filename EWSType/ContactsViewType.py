##
# Definition of the ContactsViewType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the ContactsViewType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_ContactsViewType (EWSType):
	##
	# InitialName property
	#
	# @var string
	#
	self.InitialName=''
	##
	# FinalName property
	#
	# @var string
	#
	self.FinalName=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'InitialName',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'FinalName',
		'required' : False,
		'type' : 'string',
		},
		]
# end this->schema
# end function __construct()
# end class ContactsViewType
