##
# Definition of the RecurrenceRangeBaseType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the RecurrenceRangeBaseType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_RecurrenceRangeBaseType (EWSType):
	##
	# StartDate property
	#
	# @var EWSType_date
	#
	self.StartDate=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'StartDate',
		'required' : False,
		'type' : 'date',
		},
		]
# end this->schema
# end function __construct()
# end class RecurrenceRangeBaseType
