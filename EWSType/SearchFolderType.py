##
# Definition of the SearchFolderType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the SearchFolderType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_SearchFolderType (EWSType):
	##
	# SearchParameters property
	#
	# @var EWSType_SearchParametersType
	#
	self.SearchParameters=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'SearchParameters',
		'required' : False,
		'type' : 'SearchParametersType',
		},
		]
# end this->schema
# end function __construct()
# end class SearchFolderType
