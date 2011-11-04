##
# Definition of the FileAttachmentType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the FileAttachmentType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_FileAttachmentType (EWSType):
	##
	# Content property
	#
	# @var EWSType_base64Binary
	#
	self.Content=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'Content',
		'required' : False,
		'type' : 'base64Binary',
		},
		]
# end this->schema
# end function __construct()
# end class FileAttachmentType
