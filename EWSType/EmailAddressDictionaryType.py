##
# Definition of the EmailAddressDictionaryType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the EmailAddressDictionaryType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_EmailAddressDictionaryType (EWSType):
	##
	# Entry property
	#
	# @var EWSType_EmailAddressDictionaryEntryType
	#
	self.Entry=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'Entry',
		'required' : False,
		'type' : 'EmailAddressDictionaryEntryType',
		},
		]
# end this->schema
# end function __construct()
# end class EmailAddressDictionaryType
