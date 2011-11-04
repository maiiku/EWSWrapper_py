##
# Definition of the SyncFolderItemsResponseMessageType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the SyncFolderItemsResponseMessageType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_SyncFolderItemsResponseMessageType (EWSType):
	##
	# SyncState property
	#
	# @var string
	#
	self.SyncState=''
	##
	# IncludesLastItemInRange property
	#
	# @var EWSType_boolean
	#
	self.IncludesLastItemInRange=''
	##
	# Changes property
	#
	# @var EWSType_SyncFolderItemsChangesType
	#
	self.Changes=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'SyncState',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'IncludesLastItemInRange',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'Changes',
		'required' : False,
		'type' : 'SyncFolderItemsChangesType',
		},
		]
# end this->schema
# end function __construct()
# end class SyncFolderItemsResponseMessageType
