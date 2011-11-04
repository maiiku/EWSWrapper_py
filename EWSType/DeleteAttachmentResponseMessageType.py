##
# Definition of the DeleteAttachmentResponseMessageType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the DeleteAttachmentResponseMessageType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_DeleteAttachmentResponseMessageType (EWSType):
	##
	# RootItemId property
	#
	# @var EWSType_RootItemIdType
	#
	self.RootItemId=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'RootItemId',
		'required' : False,
		'type' : 'RootItemIdType',
		},
		]
# end this->schema
# end function __construct()
# end class DeleteAttachmentResponseMessageType
