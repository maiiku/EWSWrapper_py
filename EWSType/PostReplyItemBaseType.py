##
# Definition of the PostReplyItemBaseType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the PostReplyItemBaseType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_PostReplyItemBaseType (EWSType):
	##
	# Subject property
	#
	# @var string
	#
	self.Subject=''
	##
	# Body property
	#
	# @var EWSType_BodyType
	#
	self.Body=''
	##
	# ReferenceItemId property
	#
	# @var EWSType_ItemIdType
	#
	self.ReferenceItemId=''
	##
	# ObjectName property
	#
	# @var string
	#
	self.ObjectName=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'Subject',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'Body',
		'required' : False,
		'type' : 'BodyType',
		},
		{'name' : 'ReferenceItemId',
		'required' : False,
		'type' : 'ItemIdType',
		},
		{'name' : 'ObjectName',
		'required' : False,
		'type' : 'string',
		},
		]
# end this->schema
# end function __construct()
# end class PostReplyItemBaseType
