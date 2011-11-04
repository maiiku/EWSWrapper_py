##
# Definition of the DeleteAttachmentType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the DeleteAttachmentType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_DeleteAttachmentType (EWSType):
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
		self.schema = [{'name' : 'AttachmentIds',
		'required' : False,
		'type' : 'NonEmptyArrayOfRequestAttachmentIdsType',
		},
		]
# end this->schema
# end function __construct()
# end class DeleteAttachmentType
