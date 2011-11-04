##
# Definition of the ReplyBody type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the ReplyBody type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_ReplyBody (EWSType):
	##
	# Message property
	#
	# @var string
	#
	self.Message=''
	##
	# lang property
	#
	# @var EWSType_UNKNOWN
	#
	self.lang=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'Message',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'lang',
		'required' : False,
		'type' : 'UNKNOWN',
		},
		]
# end this->schema
# end function __construct()
# end class ReplyBody
