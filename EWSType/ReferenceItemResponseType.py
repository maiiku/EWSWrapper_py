##
# Definition of the ReferenceItemResponseType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the ReferenceItemResponseType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_ReferenceItemResponseType (EWSType):
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
		self.schema = [{'name' : 'ReferenceItemId',
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
# end class ReferenceItemResponseType
