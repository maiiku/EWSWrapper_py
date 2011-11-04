##
# Definition of the PathToUnindexedFieldType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the PathToUnindexedFieldType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_PathToUnindexedFieldType (EWSType):
	##
	# FieldURI property
	#
	# @var EWSType_UnindexedFieldURIType
	#
	self.FieldURI=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'FieldURI',
		'required' : False,
		'type' : 'UnindexedFieldURIType',
		},
		]
# end this->schema
# end function __construct()
# end class PathToUnindexedFieldType
