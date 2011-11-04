##
# Definition of the OccurrenceInfoType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the OccurrenceInfoType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_OccurrenceInfoType (EWSType):
	##
	# ItemId property
	#
	# @var EWSType_ItemIdType
	#
	self.ItemId=''
	##
	# Start property
	#
	# @var EWSType_dateTime
	#
	self.Start=''
	##
	# End property
	#
	# @var EWSType_dateTime
	#
	self.End=''
	##
	# OriginalStart property
	#
	# @var EWSType_dateTime
	#
	self.OriginalStart=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'ItemId',
		'required' : False,
		'type' : 'ItemIdType',
		},
		{'name' : 'Start',
		'required' : False,
		'type' : 'dateTime',
		},
		{'name' : 'End',
		'required' : False,
		'type' : 'dateTime',
		},
		{'name' : 'OriginalStart',
		'required' : False,
		'type' : 'dateTime',
		},
		]
# end this->schema
# end function __construct()
# end class OccurrenceInfoType
