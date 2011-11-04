##
# Definition of the PhoneNumberDictionaryType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the PhoneNumberDictionaryType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_PhoneNumberDictionaryType (EWSType):
	##
	# Entry property
	#
	# @var EWSType_PhoneNumberDictionaryEntryType
	#
	self.Entry=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'Entry',
		'required' : False,
		'type' : 'PhoneNumberDictionaryEntryType',
		},
		]
# end this->schema
# end function __construct()
# end class PhoneNumberDictionaryType
