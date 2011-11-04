##
# Definition of the ExcludesType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the ExcludesType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_ExcludesType (EWSType):
	##
	# Path property
	#
	# @var EWSType_BasePathToElementType
	#
	self.Path=''
	##
	# Bitmask property
	#
	# @var EWSType_ExcludesValueType
	#
	self.Bitmask=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'Path',
		'required' : False,
		'type' : 'BasePathToElementType',
		},
		{'name' : 'Bitmask',
		'required' : False,
		'type' : 'ExcludesValueType',
		},
		]
# end this->schema
# end function __construct()
# end class ExcludesType
