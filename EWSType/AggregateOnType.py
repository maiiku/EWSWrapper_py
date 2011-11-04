##
# Definition of the AggregateOnType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the AggregateOnType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_AggregateOnType (EWSType):
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
	# Aggregate property
	#
	# @var EWSType_AggregateType
	#
	self.Aggregate=''
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
		{'name' : 'Aggregate',
		'required' : False,
		'type' : 'AggregateType',
		},
		]
# end this->schema
# end function __construct()
# end class AggregateOnType
