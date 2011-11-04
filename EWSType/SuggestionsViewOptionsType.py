##
# Definition of the SuggestionsViewOptionsType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the SuggestionsViewOptionsType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_SuggestionsViewOptionsType (EWSType):
	##
	# GoodThreshold property
	#
	# @var EWSType_int
	#
	self.GoodThreshold=''
	##
	# MaximumResultsByDay property
	#
	# @var EWSType_int
	#
	self.MaximumResultsByDay=''
	##
	# MaximumNonWorkHourResultsByDay property
	#
	# @var EWSType_int
	#
	self.MaximumNonWorkHourResultsByDay=''
	##
	# MeetingDurationInMinutes property
	#
	# @var EWSType_int
	#
	self.MeetingDurationInMinutes=''
	##
	# MinimumSuggestionQuality property
	#
	# @var EWSType_SuggestionQuality
	#
	self.MinimumSuggestionQuality=''
	##
	# DetailedSuggestionsWindow property
	#
	# @var EWSType_Duration
	#
	self.DetailedSuggestionsWindow=''
	##
	# CurrentMeetingTime property
	#
	# @var EWSType_dateTime
	#
	self.CurrentMeetingTime=''
	##
	# GlobalObjectId property
	#
	# @var string
	#
	self.GlobalObjectId=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'GoodThreshold',
		'required' : False,
		'type' : 'int',
		},
		{'name' : 'MaximumResultsByDay',
		'required' : False,
		'type' : 'int',
		},
		{'name' : 'MaximumNonWorkHourResultsByDay',
		'required' : False,
		'type' : 'int',
		},
		{'name' : 'MeetingDurationInMinutes',
		'required' : False,
		'type' : 'int',
		},
		{'name' : 'MinimumSuggestionQuality',
		'required' : False,
		'type' : 'SuggestionQuality',
		},
		{'name' : 'DetailedSuggestionsWindow',
		'required' : False,
		'type' : 'Duration',
		},
		{'name' : 'CurrentMeetingTime',
		'required' : False,
		'type' : 'dateTime',
		},
		{'name' : 'GlobalObjectId',
		'required' : False,
		'type' : 'string',
		},
		]
# end this->schema
# end function __construct()
# end class SuggestionsViewOptionsType
