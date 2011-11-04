##
# Definition of the PostItemType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the PostItemType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_PostItemType (EWSType):
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
	# PostedTime property
	#
	# @var EWSType_dateTime
	#
	self.PostedTime=''
	##
	# References property
	#
	# @var string
	#
	self.References=''
	##
	# Sender property
	#
	# @var EWSType_SingleRecipientType
	#
	self.Sender=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'ConversationIndex',
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
		{'name' : 'PostedTime',
		'required' : False,
		'type' : 'dateTime',
		},
		{'name' : 'References',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'Sender',
		'required' : False,
		'type' : 'SingleRecipientType',
		},
		]
# end this->schema
# end function __construct()
# end class PostItemType
