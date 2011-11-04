##
# Definition of the ArrayOfSuggestionDayResult type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the ArrayOfSuggestionDayResult type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_ArrayOfSuggestionDayResult (EWSType):
	##
	# SuggestionDayResult property
	#
	# @var EWSType_SuggestionDayResult
	#
	self.SuggestionDayResult=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'SuggestionDayResult',
		'required' : False,
		'type' : 'SuggestionDayResult',
		},
		]
# end this->schema
# end function __construct()
# end class ArrayOfSuggestionDayResult
