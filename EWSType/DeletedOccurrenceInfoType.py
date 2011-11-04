##
# Definition of the DeletedOccurrenceInfoType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the DeletedOccurrenceInfoType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_DeletedOccurrenceInfoType (EWSType):
	##
	# Start property
	#
	# @var EWSType_dateTime
	#
	self.Start=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'Start',
		'required' : False,
		'type' : 'dateTime',
		},
		]
# end this->schema
# end function __construct()
# end class DeletedOccurrenceInfoType
