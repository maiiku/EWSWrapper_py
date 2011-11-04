##
# Definition of the PhysicalAddressDictionaryType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the PhysicalAddressDictionaryType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_PhysicalAddressDictionaryType (EWSType):
	##
	# Entry property
	#
	# @var EWSType_PhysicalAddressDictionaryEntryType
	#
	self.Entry=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'Entry',
		'required' : False,
		'type' : 'PhysicalAddressDictionaryEntryType',
		},
		]
# end this->schema
# end function __construct()
# end class PhysicalAddressDictionaryType
