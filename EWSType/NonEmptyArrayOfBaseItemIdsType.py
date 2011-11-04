##
# Definition of the NonEmptyArrayOfBaseItemIdsType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the NonEmptyArrayOfBaseItemIdsType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_NonEmptyArrayOfBaseItemIdsType (EWSType):
	##
	# ItemId property
	#
	# @var EWSType_ItemIdType
	#
	self.ItemId=''
	##
	# OccurrenceItemId property
	#
	# @var EWSType_OccurrenceItemIdType
	#
	self.OccurrenceItemId=''
	##
	# RecurringMasterItemId property
	#
	# @var EWSType_RecurringMasterItemIdType
	#
	self.RecurringMasterItemId=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'ItemId',
		'required' : False,
		'type' : 'ItemIdType',
		},
		{'name' : 'OccurrenceItemId',
		'required' : False,
		'type' : 'OccurrenceItemIdType',
		},
		{'name' : 'RecurringMasterItemId',
		'required' : False,
		'type' : 'RecurringMasterItemIdType',
		},
		]
# end this->schema
# end function __construct()
# end class NonEmptyArrayOfBaseItemIdsType
