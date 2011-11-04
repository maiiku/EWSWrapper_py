##
# Definition of the ArrayOfSuggestion type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the ArrayOfSuggestion type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_ArrayOfSuggestion (EWSType):
	##
	# Suggestion property
	#
	# @var EWSType_Suggestion
	#
	self.Suggestion=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'Suggestion',
		'required' : False,
		'type' : 'Suggestion',
		},
		]
# end this->schema
# end function __construct()
# end class ArrayOfSuggestion
