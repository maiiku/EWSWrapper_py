##
# Definition of the AttachmentIdType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the AttachmentIdType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_AttachmentIdType (EWSType):
	##
	# RootItemId property
	#
	# @var string
	#
	self.RootItemId=''
	##
	# RootItemChangeKey property
	#
	# @var string
	#
	self.RootItemChangeKey=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'RootItemId',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'RootItemChangeKey',
		'required' : False,
		'type' : 'string',
		},
		]
# end this->schema
# end function __construct()
# end class AttachmentIdType
