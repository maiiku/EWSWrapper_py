##
# Definition of the GetAttachmentType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the GetAttachmentType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_GetAttachmentType (EWSType):
	##
	# AttachmentShape property
	#
	# @var EWSType_AttachmentResponseShapeType
	#
	self.AttachmentShape=''
	##
	# AttachmentIds property
	#
	# @var EWSType_NonEmptyArrayOfRequestAttachmentIdsType
	#
	self.AttachmentIds=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'AttachmentShape',
		'required' : False,
		'type' : 'AttachmentResponseShapeType',
		},
		{'name' : 'AttachmentIds',
		'required' : False,
		'type' : 'NonEmptyArrayOfRequestAttachmentIdsType',
		},
		]
# end this->schema
# end function __construct()
# end class GetAttachmentType
