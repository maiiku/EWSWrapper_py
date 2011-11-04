##
# Definition of the ItemType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the ItemType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_ItemType (EWSType):
	##
	# MimeContent property
	#
	# @var EWSType_MimeContentType
	#
	self.MimeContent=''
	##
	# ItemId property
	#
	# @var EWSType_ItemIdType
	#
	self.ItemId=''
	##
	# ParentFolderId property
	#
	# @var EWSType_FolderIdType
	#
	self.ParentFolderId=''
	##
	# ItemClass property
	#
	# @var EWSType_ItemClassType
	#
	self.ItemClass=''
	##
	# Subject property
	#
	# @var string
	#
	self.Subject=''
	##
	# Sensitivity property
	#
	# @var EWSType_SensitivityChoicesType
	#
	self.Sensitivity=''
	##
	# Body property
	#
	# @var EWSType_BodyType
	#
	self.Body=''
	##
	# Attachments property
	#
	# @var EWSType_NonEmptyArrayOfAttachmentsType
	#
	self.Attachments=''
	##
	# DateTimeReceived property
	#
	# @var EWSType_dateTime
	#
	self.DateTimeReceived=''
	##
	# Size property
	#
	# @var EWSType_int
	#
	self.Size=''
	##
	# Categories property
	#
	# @var EWSType_ArrayOfStringsType
	#
	self.Categories=''
	##
	# Importance property
	#
	# @var EWSType_ImportanceChoicesType
	#
	self.Importance=''
	##
	# InReplyTo property
	#
	# @var string
	#
	self.InReplyTo=''
	##
	# IsSubmitted property
	#
	# @var EWSType_boolean
	#
	self.IsSubmitted=''
	##
	# IsDraft property
	#
	# @var EWSType_boolean
	#
	self.IsDraft=''
	##
	# IsFromMe property
	#
	# @var EWSType_boolean
	#
	self.IsFromMe=''
	##
	# IsResend property
	#
	# @var EWSType_boolean
	#
	self.IsResend=''
	##
	# IsUnmodified property
	#
	# @var EWSType_boolean
	#
	self.IsUnmodified=''
	##
	# InternetMessageHeaders property
	#
	# @var EWSType_NonEmptyArrayOfInternetHeadersType
	#
	self.InternetMessageHeaders=''
	##
	# DateTimeSent property
	#
	# @var EWSType_dateTime
	#
	self.DateTimeSent=''
	##
	# DateTimeCreated property
	#
	# @var EWSType_dateTime
	#
	self.DateTimeCreated=''
	##
	# ResponseObjects property
	#
	# @var EWSType_NonEmptyArrayOfResponseObjectsType
	#
	self.ResponseObjects=''
	##
	# ReminderDueBy property
	#
	# @var EWSType_dateTime
	#
	self.ReminderDueBy=''
	##
	# ReminderIsSet property
	#
	# @var EWSType_boolean
	#
	self.ReminderIsSet=''
	##
	# ReminderMinutesBeforeStart property
	#
	# @var EWSType_ReminderMinutesBeforeStartType
	#
	self.ReminderMinutesBeforeStart=''
	##
	# DisplayCc property
	#
	# @var string
	#
	self.DisplayCc=''
	##
	# DisplayTo property
	#
	# @var string
	#
	self.DisplayTo=''
	##
	# HasAttachments property
	#
	# @var EWSType_boolean
	#
	self.HasAttachments=''
	##
	# ExtendedProperty property
	#
	# @var EWSType_ExtendedPropertyType
	#
	self.ExtendedProperty=''
	##
	# Culture property
	#
	# @var EWSType_language
	#
	self.Culture=''
	##
	# EffectiveRights property
	#
	# @var EWSType_EffectiveRightsType
	#
	self.EffectiveRights=''
	##
	# LastModifiedName property
	#
	# @var string
	#
	self.LastModifiedName=''
	##
	# LastModifiedTime property
	#
	# @var EWSType_dateTime
	#
	self.LastModifiedTime=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'MimeContent',
		'required' : False,
		'type' : 'MimeContentType',
		},
		{'name' : 'ItemId',
		'required' : False,
		'type' : 'ItemIdType',
		},
		{'name' : 'ParentFolderId',
		'required' : False,
		'type' : 'FolderIdType',
		},
		{'name' : 'ItemClass',
		'required' : False,
		'type' : 'ItemClassType',
		},
		{'name' : 'Subject',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'Sensitivity',
		'required' : False,
		'type' : 'SensitivityChoicesType',
		},
		{'name' : 'Body',
		'required' : False,
		'type' : 'BodyType',
		},
		{'name' : 'Attachments',
		'required' : False,
		'type' : 'NonEmptyArrayOfAttachmentsType',
		},
		{'name' : 'DateTimeReceived',
		'required' : False,
		'type' : 'dateTime',
		},
		{'name' : 'Size',
		'required' : False,
		'type' : 'int',
		},
		{'name' : 'Categories',
		'required' : False,
		'type' : 'ArrayOfStringsType',
		},
		{'name' : 'Importance',
		'required' : False,
		'type' : 'ImportanceChoicesType',
		},
		{'name' : 'InReplyTo',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'IsSubmitted',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'IsDraft',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'IsFromMe',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'IsResend',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'IsUnmodified',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'InternetMessageHeaders',
		'required' : False,
		'type' : 'NonEmptyArrayOfInternetHeadersType',
		},
		{'name' : 'DateTimeSent',
		'required' : False,
		'type' : 'dateTime',
		},
		{'name' : 'DateTimeCreated',
		'required' : False,
		'type' : 'dateTime',
		},
		{'name' : 'ResponseObjects',
		'required' : False,
		'type' : 'NonEmptyArrayOfResponseObjectsType',
		},
		{'name' : 'ReminderDueBy',
		'required' : False,
		'type' : 'dateTime',
		},
		{'name' : 'ReminderIsSet',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'ReminderMinutesBeforeStart',
		'required' : False,
		'type' : 'ReminderMinutesBeforeStartType',
		},
		{'name' : 'DisplayCc',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'DisplayTo',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'HasAttachments',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'ExtendedProperty',
		'required' : False,
		'type' : 'ExtendedPropertyType',
		},
		{'name' : 'Culture',
		'required' : False,
		'type' : 'language',
		},
		{'name' : 'EffectiveRights',
		'required' : False,
		'type' : 'EffectiveRightsType',
		},
		{'name' : 'LastModifiedName',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'LastModifiedTime',
		'required' : False,
		'type' : 'dateTime',
		},
		]
# end this->schema
# end function __construct()
# end class ItemType
