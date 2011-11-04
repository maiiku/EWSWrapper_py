##
# Definition of the SearchParametersType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the SearchParametersType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_SearchParametersType (EWSType):
	##
	# Restriction property
	#
	# @var EWSType_RestrictionType
	#
	self.Restriction=''
	##
	# BaseFolderIds property
	#
	# @var EWSType_NonEmptyArrayOfBaseFolderIdsType
	#
	self.BaseFolderIds=''
	##
	# Traversal property
	#
	# @var EWSType_SearchFolderTraversalType
	#
	self.Traversal=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'Restriction',
		'required' : False,
		'type' : 'RestrictionType',
		},
		{'name' : 'BaseFolderIds',
		'required' : False,
		'type' : 'NonEmptyArrayOfBaseFolderIdsType',
		},
		{'name' : 'Traversal',
		'required' : False,
		'type' : 'SearchFolderTraversalType',
		},
		]
# end this->schema
# end function __construct()
# end class SearchParametersType
