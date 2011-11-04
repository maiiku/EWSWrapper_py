##
# Definition of the ServerVersionInfo type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the ServerVersionInfo type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_ServerVersionInfo (EWSType):
	##
	# MajorVersion property
	#
	# @var EWSType_int
	#
	self.MajorVersion=''
	##
	# MinorVersion property
	#
	# @var EWSType_int
	#
	self.MinorVersion=''
	##
	# MajorBuildNumber property
	#
	# @var EWSType_int
	#
	self.MajorBuildNumber=''
	##
	# MinorBuildNumber property
	#
	# @var EWSType_int
	#
	self.MinorBuildNumber=''
	##
	# Version property
	#
	# @var string
	#
	self.Version=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'MajorVersion',
		'required' : False,
		'type' : 'int',
		},
		{'name' : 'MinorVersion',
		'required' : False,
		'type' : 'int',
		},
		{'name' : 'MajorBuildNumber',
		'required' : False,
		'type' : 'int',
		},
		{'name' : 'MinorBuildNumber',
		'required' : False,
		'type' : 'int',
		},
		{'name' : 'Version',
		'required' : False,
		'type' : 'string',
		},
		]
# end this->schema
# end function __construct()
# end class ServerVersionInfo
