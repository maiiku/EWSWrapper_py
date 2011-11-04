##
# Definition of the AttachmentResponseShapeType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the AttachmentResponseShapeType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_AttachmentResponseShapeType (EWSType):
	##
	# IncludeMimeContent property
	#
	# @var EWSType_boolean
	#
	self.IncludeMimeContent=''
	##
	# BodyType property
	#
	# @var EWSType_BodyTypeResponseType
	#
	self.BodyType=''
	##
	# AdditionalProperties property
	#
	# @var EWSType_NonEmptyArrayOfPathsToElementType
	#
	self.AdditionalProperties=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'IncludeMimeContent',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'BodyType',
		'required' : False,
		'type' : 'BodyTypeResponseType',
		},
		{'name' : 'AdditionalProperties',
		'required' : False,
		'type' : 'NonEmptyArrayOfPathsToElementType',
		},
		]
# end this->schema
# end function __construct()
# end class AttachmentResponseShapeType
