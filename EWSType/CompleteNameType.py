##
# Definition of the CompleteNameType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the CompleteNameType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_CompleteNameType (EWSType):
	##
	# Title property
	#
	# @var string
	#
	self.Title=''
	##
	# FirstName property
	#
	# @var string
	#
	self.FirstName=''
	##
	# MiddleName property
	#
	# @var string
	#
	self.MiddleName=''
	##
	# LastName property
	#
	# @var string
	#
	self.LastName=''
	##
	# Suffix property
	#
	# @var string
	#
	self.Suffix=''
	##
	# Initials property
	#
	# @var string
	#
	self.Initials=''
	##
	# FullName property
	#
	# @var string
	#
	self.FullName=''
	##
	# Nickname property
	#
	# @var string
	#
	self.Nickname=''
	##
	# YomiFirstName property
	#
	# @var string
	#
	self.YomiFirstName=''
	##
	# YomiLastName property
	#
	# @var string
	#
	self.YomiLastName=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'Title',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'FirstName',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'MiddleName',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'LastName',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'Suffix',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'Initials',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'FullName',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'Nickname',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'YomiFirstName',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'YomiLastName',
		'required' : False,
		'type' : 'string',
		},
		]
# end this->schema
# end function __construct()
# end class CompleteNameType
