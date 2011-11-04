##
# Definition of the MessageType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the MessageType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_MessageType (EWSType):
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
	# ConversationIndex property
	#
	# @var EWSType_base64Binary
	#
	self.ConversationIndex=''
	##
	# ConversationTopic property
	#
	# @var string
	#
	self.ConversationTopic=''
	##
	# From property
	#
	# @var EWSType_SingleRecipientType
	#
	self.From=''
	##
	# InternetMessageId property
	#
	# @var string
	#
	self.InternetMessageId=''
	##
	# IsRead property
	#
	# @var EWSType_boolean
	#
	self.IsRead=''
	##
	# IsResponseRequested property
	#
	# @var EWSType_boolean
	#
	self.IsResponseRequested=''
	##
	# References property
	#
	# @var string
	#
	self.References=''
	##
	# ReplyTo property
	#
	# @var EWSType_ArrayOfRecipientsType
	#
	self.ReplyTo=''
	##
	# ReceivedBy property
	#
	# @var EWSType_SingleRecipientType
	#
	self.ReceivedBy=''
	##
	# ReceivedRepresenting property
	#
	# @var EWSType_SingleRecipientType
	#
	self.ReceivedRepresenting=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'Sender',
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
		{'name' : 'ConversationIndex',
		'required' : False,
		'type' : 'base64Binary',
		},
		{'name' : 'ConversationTopic',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'From',
		'required' : False,
		'type' : 'SingleRecipientType',
		},
		{'name' : 'InternetMessageId',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'IsRead',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'IsResponseRequested',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'References',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'ReplyTo',
		'required' : False,
		'type' : 'ArrayOfRecipientsType',
		},
		{'name' : 'ReceivedBy',
		'required' : False,
		'type' : 'SingleRecipientType',
		},
		{'name' : 'ReceivedRepresenting',
		'required' : False,
		'type' : 'SingleRecipientType',
		},
		]
# end this->schema
# end function __construct()
# end class MessageType
