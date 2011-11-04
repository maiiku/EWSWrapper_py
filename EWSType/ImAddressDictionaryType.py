##
# Definition of the ImAddressDictionaryType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the ImAddressDictionaryType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_ImAddressDictionaryType (EWSType):
	##
	# Entry property
	#
	# @var EWSType_ImAddressDictionaryEntryType
	#
	self.Entry=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'Entry',
		'required' : False,
		'type' : 'ImAddressDictionaryEntryType',
		},
		]
# end this->schema
# end function __construct()
# end class ImAddressDictionaryType
