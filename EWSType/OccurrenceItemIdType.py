##
# Definition of the OccurrenceItemIdType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the OccurrenceItemIdType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_OccurrenceItemIdType (EWSType):
	##
	# RecurringMasterId property
	#
	# @var EWSType_DerivedItemIdType
	#
	self.RecurringMasterId=''
	##
	# ChangeKey property
	#
	# @var string
	#
	self.ChangeKey=''
	##
	# InstanceIndex property
	#
	# @var EWSType_int
	#
	self.InstanceIndex=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'RecurringMasterId',
		'required' : False,
		'type' : 'DerivedItemIdType',
		},
		{'name' : 'ChangeKey',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'InstanceIndex',
		'required' : False,
		'type' : 'int',
		},
		]
# end this->schema
# end function __construct()
# end class OccurrenceItemIdType
