##
# Definition of the ConvertIdResponseMessageType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the ConvertIdResponseMessageType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_ConvertIdResponseMessageType (EWSType):
	##
	# AlternateId property
	#
	# @var EWSType_AlternateIdBaseType
	#
	self.AlternateId=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'AlternateId',
		'required' : False,
		'type' : 'AlternateIdBaseType',
		},
		]
# end this->schema
# end function __construct()
# end class ConvertIdResponseMessageType
