##
# Definition of the EndDateRecurrenceRangeType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the EndDateRecurrenceRangeType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_EndDateRecurrenceRangeType (EWSType):
	##
	# EndDate property
	#
	# @var EWSType_date
	#
	self.EndDate=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'EndDate',
		'required' : False,
		'type' : 'date',
		},
		]
# end this->schema
# end function __construct()
# end class EndDateRecurrenceRangeType
