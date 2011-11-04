##
# Definition of the NonEmptyArrayOfDeletedOccurrencesType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the NonEmptyArrayOfDeletedOccurrencesType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_NonEmptyArrayOfDeletedOccurrencesType (EWSType):
	##
	# DeletedOccurrence property
	#
	# @var EWSType_DeletedOccurrenceInfoType
	#
	self.DeletedOccurrence=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'DeletedOccurrence',
		'required' : False,
		'type' : 'DeletedOccurrenceInfoType',
		},
		]
# end this->schema
# end function __construct()
# end class NonEmptyArrayOfDeletedOccurrencesType
