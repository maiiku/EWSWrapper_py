##
# Definition of the ResponseObjectCoreType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the ResponseObjectCoreType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_ResponseObjectCoreType (EWSType):
	##
	# ReferenceItemId property
	#
	# @var EWSType_ItemIdType
	#
	self.ReferenceItemId=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'ReferenceItemId',
		'required' : False,
		'type' : 'ItemIdType',
		},
		]
# end this->schema
# end function __construct()
# end class ResponseObjectCoreType
