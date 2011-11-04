##
# Definition of the SmartResponseBaseType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the SmartResponseBaseType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_SmartResponseBaseType (EWSType):
	##
	# Subject property
	#
	# @var string
	#
	self.Subject=''
	##
	# Body property
	#
	# @var EWSType_BodyType
	#
	self.Body=''
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
		self.schema = [{'name' : 'Subject',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'Body',
		'required' : False,
		'type' : 'BodyType',
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
# end class SmartResponseBaseType
