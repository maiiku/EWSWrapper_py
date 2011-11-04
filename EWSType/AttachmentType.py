##
# Definition of the AttachmentType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the AttachmentType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_AttachmentType (EWSType):
	##
	# AttachmentId property
	#
	# @var EWSType_AttachmentIdType
	#
	self.AttachmentId=''
	##
	# Name property
	#
	# @var string
	#
	self.Name=''
	##
	# ContentType property
	#
	# @var string
	#
	self.ContentType=''
	##
	# ContentId property
	#
	# @var string
	#
	self.ContentId=''
	##
	# ContentLocation property
	#
	# @var string
	#
	self.ContentLocation=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'AttachmentId',
		'required' : False,
		'type' : 'AttachmentIdType',
		},
		{'name' : 'Name',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'ContentType',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'ContentId',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'ContentLocation',
		'required' : False,
		'type' : 'string',
		},
		]
# end this->schema
# end function __construct()
# end class AttachmentType
