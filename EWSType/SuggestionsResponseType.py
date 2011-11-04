##
# Definition of the SuggestionsResponseType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the SuggestionsResponseType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_SuggestionsResponseType (EWSType):
	##
	# ResponseMessage property
	#
	# @var EWSType_ResponseMessageType
	#
	self.ResponseMessage=''
	##
	# SuggestionDayResultArray property
	#
	# @var EWSType_ArrayOfSuggestionDayResult
	#
	self.SuggestionDayResultArray=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'ResponseMessage',
		'required' : False,
		'type' : 'ResponseMessageType',
		},
		{'name' : 'SuggestionDayResultArray',
		'required' : False,
		'type' : 'ArrayOfSuggestionDayResult',
		},
		]
# end this->schema
# end function __construct()
# end class SuggestionsResponseType
