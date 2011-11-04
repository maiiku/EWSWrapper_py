##
# Definition of the ArrayOfResponseMessagesType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the ArrayOfResponseMessagesType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_ArrayOfResponseMessagesType (EWSType):
	##
	# CreateItemResponseMessage property
	#
	# @var EWSType_ItemInfoResponseMessageType
	#
	self.CreateItemResponseMessage=''
	##
	# DeleteItemResponseMessage property
	#
	# @var EWSType_ResponseMessageType
	#
	self.DeleteItemResponseMessage=''
	##
	# GetItemResponseMessage property
	#
	# @var EWSType_ItemInfoResponseMessageType
	#
	self.GetItemResponseMessage=''
	##
	# UpdateItemResponseMessage property
	#
	# @var EWSType_UpdateItemResponseMessageType
	#
	self.UpdateItemResponseMessage=''
	##
	# SendItemResponseMessage property
	#
	# @var EWSType_ResponseMessageType
	#
	self.SendItemResponseMessage=''
	##
	# DeleteFolderResponseMessage property
	#
	# @var EWSType_ResponseMessageType
	#
	self.DeleteFolderResponseMessage=''
	##
	# CreateFolderResponseMessage property
	#
	# @var EWSType_FolderInfoResponseMessageType
	#
	self.CreateFolderResponseMessage=''
	##
	# GetFolderResponseMessage property
	#
	# @var EWSType_FolderInfoResponseMessageType
	#
	self.GetFolderResponseMessage=''
	##
	# FindFolderResponseMessage property
	#
	# @var EWSType_FindFolderResponseMessageType
	#
	self.FindFolderResponseMessage=''
	##
	# UpdateFolderResponseMessage property
	#
	# @var EWSType_FolderInfoResponseMessageType
	#
	self.UpdateFolderResponseMessage=''
	##
	# MoveFolderResponseMessage property
	#
	# @var EWSType_FolderInfoResponseMessageType
	#
	self.MoveFolderResponseMessage=''
	##
	# CopyFolderResponseMessage property
	#
	# @var EWSType_FolderInfoResponseMessageType
	#
	self.CopyFolderResponseMessage=''
	##
	# CreateAttachmentResponseMessage property
	#
	# @var EWSType_AttachmentInfoResponseMessageType
	#
	self.CreateAttachmentResponseMessage=''
	##
	# DeleteAttachmentResponseMessage property
	#
	# @var EWSType_DeleteAttachmentResponseMessageType
	#
	self.DeleteAttachmentResponseMessage=''
	##
	# GetAttachmentResponseMessage property
	#
	# @var EWSType_AttachmentInfoResponseMessageType
	#
	self.GetAttachmentResponseMessage=''
	##
	# FindItemResponseMessage property
	#
	# @var EWSType_FindItemResponseMessageType
	#
	self.FindItemResponseMessage=''
	##
	# MoveItemResponseMessage property
	#
	# @var EWSType_ItemInfoResponseMessageType
	#
	self.MoveItemResponseMessage=''
	##
	# CopyItemResponseMessage property
	#
	# @var EWSType_ItemInfoResponseMessageType
	#
	self.CopyItemResponseMessage=''
	##
	# ResolveNamesResponseMessage property
	#
	# @var EWSType_ResolveNamesResponseMessageType
	#
	self.ResolveNamesResponseMessage=''
	##
	# ExpandDLResponseMessage property
	#
	# @var EWSType_ExpandDLResponseMessageType
	#
	self.ExpandDLResponseMessage=''
	##
	# GetEventsResponseMessage property
	#
	# @var EWSType_GetEventsResponseMessageType
	#
	self.GetEventsResponseMessage=''
	##
	# SubscribeResponseMessage property
	#
	# @var EWSType_SubscribeResponseMessageType
	#
	self.SubscribeResponseMessage=''
	##
	# UnsubscribeResponseMessage property
	#
	# @var EWSType_ResponseMessageType
	#
	self.UnsubscribeResponseMessage=''
	##
	# SendNotificationResponseMessage property
	#
	# @var EWSType_SendNotificationResponseMessageType
	#
	self.SendNotificationResponseMessage=''
	##
	# SyncFolderHierarchyResponseMessage property
	#
	# @var EWSType_SyncFolderHierarchyResponseMessageType
	#
	self.SyncFolderHierarchyResponseMessage=''
	##
	# SyncFolderItemsResponseMessage property
	#
	# @var EWSType_SyncFolderItemsResponseMessageType
	#
	self.SyncFolderItemsResponseMessage=''
	##
	# CreateManagedFolderResponseMessage property
	#
	# @var EWSType_FolderInfoResponseMessageType
	#
	self.CreateManagedFolderResponseMessage=''
	##
	# ConvertIdResponseMessage property
	#
	# @var EWSType_ConvertIdResponseMessageType
	#
	self.ConvertIdResponseMessage=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'CreateItemResponseMessage',
		'required' : False,
		'type' : 'ItemInfoResponseMessageType',
		},
		{'name' : 'DeleteItemResponseMessage',
		'required' : False,
		'type' : 'ResponseMessageType',
		},
		{'name' : 'GetItemResponseMessage',
		'required' : False,
		'type' : 'ItemInfoResponseMessageType',
		},
		{'name' : 'UpdateItemResponseMessage',
		'required' : False,
		'type' : 'UpdateItemResponseMessageType',
		},
		{'name' : 'SendItemResponseMessage',
		'required' : False,
		'type' : 'ResponseMessageType',
		},
		{'name' : 'DeleteFolderResponseMessage',
		'required' : False,
		'type' : 'ResponseMessageType',
		},
		{'name' : 'CreateFolderResponseMessage',
		'required' : False,
		'type' : 'FolderInfoResponseMessageType',
		},
		{'name' : 'GetFolderResponseMessage',
		'required' : False,
		'type' : 'FolderInfoResponseMessageType',
		},
		{'name' : 'FindFolderResponseMessage',
		'required' : False,
		'type' : 'FindFolderResponseMessageType',
		},
		{'name' : 'UpdateFolderResponseMessage',
		'required' : False,
		'type' : 'FolderInfoResponseMessageType',
		},
		{'name' : 'MoveFolderResponseMessage',
		'required' : False,
		'type' : 'FolderInfoResponseMessageType',
		},
		{'name' : 'CopyFolderResponseMessage',
		'required' : False,
		'type' : 'FolderInfoResponseMessageType',
		},
		{'name' : 'CreateAttachmentResponseMessage',
		'required' : False,
		'type' : 'AttachmentInfoResponseMessageType',
		},
		{'name' : 'DeleteAttachmentResponseMessage',
		'required' : False,
		'type' : 'DeleteAttachmentResponseMessageType',
		},
		{'name' : 'GetAttachmentResponseMessage',
		'required' : False,
		'type' : 'AttachmentInfoResponseMessageType',
		},
		{'name' : 'FindItemResponseMessage',
		'required' : False,
		'type' : 'FindItemResponseMessageType',
		},
		{'name' : 'MoveItemResponseMessage',
		'required' : False,
		'type' : 'ItemInfoResponseMessageType',
		},
		{'name' : 'CopyItemResponseMessage',
		'required' : False,
		'type' : 'ItemInfoResponseMessageType',
		},
		{'name' : 'ResolveNamesResponseMessage',
		'required' : False,
		'type' : 'ResolveNamesResponseMessageType',
		},
		{'name' : 'ExpandDLResponseMessage',
		'required' : False,
		'type' : 'ExpandDLResponseMessageType',
		},
		{'name' : 'GetEventsResponseMessage',
		'required' : False,
		'type' : 'GetEventsResponseMessageType',
		},
		{'name' : 'SubscribeResponseMessage',
		'required' : False,
		'type' : 'SubscribeResponseMessageType',
		},
		{'name' : 'UnsubscribeResponseMessage',
		'required' : False,
		'type' : 'ResponseMessageType',
		},
		{'name' : 'SendNotificationResponseMessage',
		'required' : False,
		'type' : 'SendNotificationResponseMessageType',
		},
		{'name' : 'SyncFolderHierarchyResponseMessage',
		'required' : False,
		'type' : 'SyncFolderHierarchyResponseMessageType',
		},
		{'name' : 'SyncFolderItemsResponseMessage',
		'required' : False,
		'type' : 'SyncFolderItemsResponseMessageType',
		},
		{'name' : 'CreateManagedFolderResponseMessage',
		'required' : False,
		'type' : 'FolderInfoResponseMessageType',
		},
		{'name' : 'ConvertIdResponseMessage',
		'required' : False,
		'type' : 'ConvertIdResponseMessageType',
		},
		]
# end this->schema
# end function __construct()
# end class ArrayOfResponseMessagesType
