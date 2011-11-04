##
# Definition of the FreeBusyResponseType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the FreeBusyResponseType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_FreeBusyResponseType (EWSType):
	##
	# ResponseMessage property
	#
	# @var EWSType_ResponseMessageType
	#
	self.ResponseMessage=''
	##
	# FreeBusyView property
	#
	# @var EWSType_FreeBusyView
	#
	self.FreeBusyView=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'ResponseMessage',
		'required' : False,
		'type' : 'ResponseMessageType',
		},
		{'name' : 'FreeBusyView',
		'required' : False,
		'type' : 'FreeBusyView',
		},
		]
# end this->schema
# end function __construct()
# end class FreeBusyResponseType
