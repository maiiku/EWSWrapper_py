##
# Definition of the UpdateItemResponseMessageType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the UpdateItemResponseMessageType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_UpdateItemResponseMessageType (EWSType):
	##
	# ConflictResults property
	#
	# @var EWSType_ConflictResultsType
	#
	self.ConflictResults=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'ConflictResults',
		'required' : False,
		'type' : 'ConflictResultsType',
		},
		]
# end this->schema
# end function __construct()
# end class UpdateItemResponseMessageType
