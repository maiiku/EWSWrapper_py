##
# Definition of the NonEmptyArrayOfAttachmentsType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the NonEmptyArrayOfAttachmentsType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_NonEmptyArrayOfAttachmentsType (EWSType):
	##
	# ItemAttachment property
	#
	# @var EWSType_ItemAttachmentType
	#
	self.ItemAttachment=''
	##
	# FileAttachment property
	#
	# @var EWSType_FileAttachmentType
	#
	self.FileAttachment=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'ItemAttachment',
		'required' : False,
		'type' : 'ItemAttachmentType',
		},
		{'name' : 'FileAttachment',
		'required' : False,
		'type' : 'FileAttachmentType',
		},
		]
# end this->schema
# end function __construct()
# end class NonEmptyArrayOfAttachmentsType
