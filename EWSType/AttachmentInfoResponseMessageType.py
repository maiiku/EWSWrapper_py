##
# Definition of the AttachmentInfoResponseMessageType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the AttachmentInfoResponseMessageType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_AttachmentInfoResponseMessageType (EWSType):
	##
	# Attachments property
	#
	# @var EWSType_ArrayOfAttachmentsType
	#
	self.Attachments=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'Attachments',
		'required' : False,
		'type' : 'ArrayOfAttachmentsType',
		},
		]
# end this->schema
# end function __construct()
# end class AttachmentInfoResponseMessageType
