##
# Definition of the ResolveNamesType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the ResolveNamesType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_ResolveNamesType (EWSType):
	##
	# ParentFolderIds property
	#
	# @var EWSType_NonEmptyArrayOfBaseFolderIdsType
	#
	self.ParentFolderIds=''
	##
	# UnresolvedEntry property
	#
	# @var EWSType_NonEmptyStringType
	#
	self.UnresolvedEntry=''
	##
	# ReturnFullContactData property
	#
	# @var EWSType_boolean
	#
	self.ReturnFullContactData=''
	##
	# SearchScope property
	#
	# @var EWSType_ResolveNamesSearchScopeType
	#
	self.SearchScope=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'ParentFolderIds',
		'required' : False,
		'type' : 'NonEmptyArrayOfBaseFolderIdsType',
		},
		{'name' : 'UnresolvedEntry',
		'required' : False,
		'type' : 'NonEmptyStringType',
		},
		{'name' : 'ReturnFullContactData',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'SearchScope',
		'required' : False,
		'type' : 'ResolveNamesSearchScopeType',
		},
		]
# end this->schema
# end function __construct()
# end class ResolveNamesType
