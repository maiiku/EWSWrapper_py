##
# Definition of the SuggestionDayResult type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the SuggestionDayResult type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_SuggestionDayResult (EWSType):
	##
	# Date property
	#
	# @var EWSType_dateTime
	#
	self.Date=''
	##
	# DayQuality property
	#
	# @var EWSType_SuggestionQuality
	#
	self.DayQuality=''
	##
	# SuggestionArray property
	#
	# @var EWSType_ArrayOfSuggestion
	#
	self.SuggestionArray=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'Date',
		'required' : False,
		'type' : 'dateTime',
		},
		{'name' : 'DayQuality',
		'required' : False,
		'type' : 'SuggestionQuality',
		},
		{'name' : 'SuggestionArray',
		'required' : False,
		'type' : 'ArrayOfSuggestion',
		},
		]
# end this->schema
# end function __construct()
# end class SuggestionDayResult
