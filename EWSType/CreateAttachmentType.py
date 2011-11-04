##
# Definition of the CreateAttachmentType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the CreateAttachmentType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_CreateAttachmentType (EWSType):
	##
	# ParentItemId property
	#
	# @var EWSType_ItemIdType
	#
	self.ParentItemId=''
	##
	# Attachments property
	#
	# @var EWSType_NonEmptyArrayOfAttachmentsType
	#
	self.Attachments=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'ParentItemId',
		'required' : False,
		'type' : 'ItemIdType',
		},
		{'name' : 'Attachments',
		'required' : False,
		'type' : 'NonEmptyArrayOfAttachmentsType',
		},
		]
# end this->schema
# end function __construct()
# end class CreateAttachmentType
