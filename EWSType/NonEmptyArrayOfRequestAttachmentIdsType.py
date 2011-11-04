##
# Definition of the NonEmptyArrayOfRequestAttachmentIdsType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the NonEmptyArrayOfRequestAttachmentIdsType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_NonEmptyArrayOfRequestAttachmentIdsType (EWSType):
	##
	# AttachmentId property
	#
	# @var EWSType_RequestAttachmentIdType
	#
	self.AttachmentId=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'AttachmentId',
		'required' : False,
		'type' : 'RequestAttachmentIdType',
		},
		]
# end this->schema
# end function __construct()
# end class NonEmptyArrayOfRequestAttachmentIdsType
