##
# Definition of the SyncFolderItemsReadFlagType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the SyncFolderItemsReadFlagType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_SyncFolderItemsReadFlagType (EWSType):
	##
	# ItemId property
	#
	# @var EWSType_ItemIdType
	#
	self.ItemId=''
	##
	# IsRead property
	#
	# @var EWSType_boolean
	#
	self.IsRead=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'ItemId',
		'required' : False,
		'type' : 'ItemIdType',
		},
		{'name' : 'IsRead',
		'required' : False,
		'type' : 'boolean',
		},
		]
# end this->schema
# end function __construct()
# end class SyncFolderItemsReadFlagType
