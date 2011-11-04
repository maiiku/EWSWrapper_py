##
# Definition of the ResponseMessageType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the ResponseMessageType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_ResponseMessageType (EWSType):
	##
	# MessageText property
	#
	# @var string
	#
	self.MessageText=''
	##
	# ResponseCode property
	#
	# @var EWSType_ResponseCodeType
	#
	self.ResponseCode=''
	##
	# DescriptiveLinkKey property
	#
	# @var EWSType_int
	#
	self.DescriptiveLinkKey=''
	##
	# MessageXml property
	#
	# @var EWSType_MessageXml
	#
	self.MessageXml=''
	##
	# ResponseClass property
	#
	# @var EWSType_ResponseClassType
	#
	self.ResponseClass=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'MessageText',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'ResponseCode',
		'required' : False,
		'type' : 'ResponseCodeType',
		},
		{'name' : 'DescriptiveLinkKey',
		'required' : False,
		'type' : 'int',
		},
		{'name' : 'MessageXml',
		'required' : False,
		'type' : 'MessageXml',
		},
		{'name' : 'ResponseClass',
		'required' : False,
		'type' : 'ResponseClassType',
		},
		]
# end this->schema
# end function __construct()
# end class ResponseMessageType
