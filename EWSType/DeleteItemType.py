##
# Definition of the DeleteItemType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the DeleteItemType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_DeleteItemType (EWSType):
	##
	# ItemIds property
	#
	# @var EWSType_NonEmptyArrayOfBaseItemIdsType
	#
	self.ItemIds=''
	##
	# DeleteType property
	#
	# @var EWSType_DisposalType
	#
	self.DeleteType=''
	##
	# SendMeetingCancellations property
	#
	# @var EWSType_CalendarItemCreateOrDeleteOperationType
	#
	self.SendMeetingCancellations=''
	##
	# AffectedTaskOccurrences property
	#
	# @var EWSType_AffectedTaskOccurrencesType
	#
	self.AffectedTaskOccurrences=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'ItemIds',
		'required' : False,
		'type' : 'NonEmptyArrayOfBaseItemIdsType',
		},
		{'name' : 'DeleteType',
		'required' : False,
		'type' : 'DisposalType',
		},
		{'name' : 'SendMeetingCancellations',
		'required' : False,
		'type' : 'CalendarItemCreateOrDeleteOperationType',
		},
		{'name' : 'AffectedTaskOccurrences',
		'required' : False,
		'type' : 'AffectedTaskOccurrencesType',
		},
		]
# end this->schema
# end function __construct()
# end class DeleteItemType
