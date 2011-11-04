##
# Definition of the ModifiedEventType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the ModifiedEventType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_ModifiedEventType (EWSType):
	##
	# UnreadCount property
	#
	# @var EWSType_int
	#
	self.UnreadCount=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'UnreadCount',
		'required' : False,
		'type' : 'int',
		},
		]
# end this->schema
# end function __construct()
# end class ModifiedEventType
