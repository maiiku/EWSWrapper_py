##
# Definition of the NonEmptyArrayOfInternetHeadersType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the NonEmptyArrayOfInternetHeadersType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_NonEmptyArrayOfInternetHeadersType (EWSType):
	##
	# InternetMessageHeader property
	#
	# @var EWSType_InternetHeaderType
	#
	self.InternetMessageHeader=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'InternetMessageHeader',
		'required' : False,
		'type' : 'InternetHeaderType',
		},
		]
# end this->schema
# end function __construct()
# end class NonEmptyArrayOfInternetHeadersType
