##
# Definition of the FreeBusyViewOptionsType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the FreeBusyViewOptionsType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_FreeBusyViewOptionsType (EWSType):
	##
	# TimeWindow property
	#
	# @var EWSType_Duration
	#
	self.TimeWindow=''
	##
	# MergedFreeBusyIntervalInMinutes property
	#
	# @var EWSType_int
	#
	self.MergedFreeBusyIntervalInMinutes=''
	##
	# RequestedView property
	#
	# @var EWSType_FreeBusyViewType
	#
	self.RequestedView=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'TimeWindow',
		'required' : False,
		'type' : 'Duration',
		},
		{'name' : 'MergedFreeBusyIntervalInMinutes',
		'required' : False,
		'type' : 'int',
		},
		{'name' : 'RequestedView',
		'required' : False,
		'type' : 'FreeBusyViewType',
		},
		]
# end this->schema
# end function __construct()
# end class FreeBusyViewOptionsType
