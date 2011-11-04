##
# Definition of the GroupByType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the GroupByType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_GroupByType (EWSType):
	##
	# FieldURI property
	#
	# @var EWSType_PathToUnindexedFieldType
	#
	self.FieldURI=''
	##
	# IndexedFieldURI property
	#
	# @var EWSType_PathToIndexedFieldType
	#
	self.IndexedFieldURI=''
	##
	# ExtendedFieldURI property
	#
	# @var EWSType_PathToExtendedFieldType
	#
	self.ExtendedFieldURI=''
	##
	# AggregateOn property
	#
	# @var EWSType_AggregateOnType
	#
	self.AggregateOn=''
	##
	# Order property
	#
	# @var EWSType_SortDirectionType
	#
	self.Order=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'FieldURI',
		'required' : False,
		'type' : 'PathToUnindexedFieldType',
		},
		{'name' : 'IndexedFieldURI',
		'required' : False,
		'type' : 'PathToIndexedFieldType',
		},
		{'name' : 'ExtendedFieldURI',
		'required' : False,
		'type' : 'PathToExtendedFieldType',
		},
		{'name' : 'AggregateOn',
		'required' : False,
		'type' : 'AggregateOnType',
		},
		{'name' : 'Order',
		'required' : True,
		'type' : 'SortDirectionType',
		},
		]
# end this->schema
# end function __construct()
# end class GroupByType
