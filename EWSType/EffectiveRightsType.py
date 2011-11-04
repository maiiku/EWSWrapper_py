##
# Definition of the EffectiveRightsType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the EffectiveRightsType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_EffectiveRightsType (EWSType):
	##
	# CreateAssociated property
	#
	# @var EWSType_boolean
	#
	self.CreateAssociated=''
	##
	# CreateContents property
	#
	# @var EWSType_boolean
	#
	self.CreateContents=''
	##
	# CreateHierarchy property
	#
	# @var EWSType_boolean
	#
	self.CreateHierarchy=''
	##
	# Delete property
	#
	# @var EWSType_boolean
	#
	self.Delete=''
	##
	# Modify property
	#
	# @var EWSType_boolean
	#
	self.Modify=''
	##
	# Read property
	#
	# @var EWSType_boolean
	#
	self.Read=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'CreateAssociated',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'CreateContents',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'CreateHierarchy',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'Delete',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'Modify',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'Read',
		'required' : False,
		'type' : 'boolean',
		},
		]
# end this->schema
# end function __construct()
# end class EffectiveRightsType
