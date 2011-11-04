##
# Definition of the ItemChangeType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the ItemChangeType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_ItemChangeType (EWSType):
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
	# Updates property
	#
	# @var EWSType_NonEmptyArrayOfItemChangeDescriptionsType
	#
	self.Updates=''
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
		{'name' : 'Updates',
		'required' : False,
		'type' : 'NonEmptyArrayOfItemChangeDescriptionsType',
		},
		]
# end this->schema
# end function __construct()
# end class ItemChangeType
