##
# Definition of the WellKnownResponseObjectType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the WellKnownResponseObjectType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_WellKnownResponseObjectType (EWSType):
	##
	# ItemClass property
	#
	# @var EWSType_ItemClassType
	#
	self.ItemClass=''
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
	# InternetMessageHeaders property
	#
	# @var EWSType_NonEmptyArrayOfInternetHeadersType
	#
	self.InternetMessageHeaders=''
	##
	# Sender property
	#
	# @var EWSType_SingleRecipientType
	#
	self.Sender=''
	##
	# ToRecipients property
	#
	# @var EWSType_ArrayOfRecipientsType
	#
	self.ToRecipients=''
	##
	# CcRecipients property
	#
	# @var EWSType_ArrayOfRecipientsType
	#
	self.CcRecipients=''
	##
	# BccRecipients property
	#
	# @var EWSType_ArrayOfRecipientsType
	#
	self.BccRecipients=''
	##
	# IsReadReceiptRequested property
	#
	# @var EWSType_boolean
	#
	self.IsReadReceiptRequested=''
	##
	# IsDeliveryReceiptRequested property
	#
	# @var EWSType_boolean
	#
	self.IsDeliveryReceiptRequested=''
	##
	# From property
	#
	# @var EWSType_SingleRecipientType
	#
	self.From=''
	##
	# ReferenceItemId property
	#
	# @var EWSType_ItemIdType
	#
	self.ReferenceItemId=''
	##
	# ObjectName property
	#
	# @var string
	#
	self.ObjectName=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'ItemClass',
		'required' : False,
		'type' : 'ItemClassType',
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
		{'name' : 'InternetMessageHeaders',
		'required' : False,
		'type' : 'NonEmptyArrayOfInternetHeadersType',
		},
		{'name' : 'Sender',
		'required' : False,
		'type' : 'SingleRecipientType',
		},
		{'name' : 'ToRecipients',
		'required' : False,
		'type' : 'ArrayOfRecipientsType',
		},
		{'name' : 'CcRecipients',
		'required' : False,
		'type' : 'ArrayOfRecipientsType',
		},
		{'name' : 'BccRecipients',
		'required' : False,
		'type' : 'ArrayOfRecipientsType',
		},
		{'name' : 'IsReadReceiptRequested',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'IsDeliveryReceiptRequested',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'From',
		'required' : False,
		'type' : 'SingleRecipientType',
		},
		{'name' : 'ReferenceItemId',
		'required' : False,
		'type' : 'ItemIdType',
		},
		{'name' : 'ObjectName',
		'required' : False,
		'type' : 'string',
		},
		]
# end this->schema
# end function __construct()
# end class WellKnownResponseObjectType
