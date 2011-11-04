##
# Definition of the MimeContentType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the MimeContentType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_MimeContentType (EWSType):
	##
	# _ property
	#
	# @var string
	#
	self._=''
	##
	# CharacterSet property
	#
	# @var string
	#
	self.CharacterSet=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : '_',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'CharacterSet',
		'required' : False,
		'type' : 'string',
		},
		]
# end this->schema
# end function __construct()
# end class MimeContentType
