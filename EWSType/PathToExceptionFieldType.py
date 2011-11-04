##
# Definition of the PathToExceptionFieldType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the PathToExceptionFieldType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_PathToExceptionFieldType (EWSType):
	##
	# FieldURI property
	#
	# @var EWSType_ExceptionPropertyURIType
	#
	self.FieldURI=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'FieldURI',
		'required' : False,
		'type' : 'ExceptionPropertyURIType',
		},
		]
# end this->schema
# end function __construct()
# end class PathToExceptionFieldType
