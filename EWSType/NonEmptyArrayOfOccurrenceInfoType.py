##
# Definition of the NonEmptyArrayOfOccurrenceInfoType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the NonEmptyArrayOfOccurrenceInfoType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_NonEmptyArrayOfOccurrenceInfoType (EWSType):
	##
	# Occurrence property
	#
	# @var EWSType_OccurrenceInfoType
	#
	self.Occurrence=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'Occurrence',
		'required' : False,
		'type' : 'OccurrenceInfoType',
		},
		]
# end this->schema
# end function __construct()
# end class NonEmptyArrayOfOccurrenceInfoType
