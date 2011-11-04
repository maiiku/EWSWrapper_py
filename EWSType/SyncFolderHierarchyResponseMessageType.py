##
# Definition of the SyncFolderHierarchyResponseMessageType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the SyncFolderHierarchyResponseMessageType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_SyncFolderHierarchyResponseMessageType (EWSType):
	##
	# SyncState property
	#
	# @var string
	#
	self.SyncState=''
	##
	# IncludesLastFolderInRange property
	#
	# @var EWSType_boolean
	#
	self.IncludesLastFolderInRange=''
	##
	# Changes property
	#
	# @var EWSType_SyncFolderHierarchyChangesType
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
		{'name' : 'IncludesLastFolderInRange',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'Changes',
		'required' : False,
		'type' : 'SyncFolderHierarchyChangesType',
		},
		]
# end this->schema
# end function __construct()
# end class SyncFolderHierarchyResponseMessageType
