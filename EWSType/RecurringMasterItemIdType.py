##
# Definition of the RecurringMasterItemIdType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the RecurringMasterItemIdType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_RecurringMasterItemIdType (EWSType):
	##
	# OccurrenceId property
	#
	# @var EWSType_DerivedItemIdType
	#
	self.OccurrenceId=''
	##
	# ChangeKey property
	#
	# @var string
	#
	self.ChangeKey=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'OccurrenceId',
		'required' : False,
		'type' : 'DerivedItemIdType',
		},
		{'name' : 'ChangeKey',
		'required' : False,
		'type' : 'string',
		},
		]
# end this->schema
# end function __construct()
# end class RecurringMasterItemIdType
