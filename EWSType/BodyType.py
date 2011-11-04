##
# Definition of the BodyType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the BodyType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_BodyType (EWSType):
	##
	# _ property
	#
	# @var string
	#
	self._=''
	##
	# BodyType property
	#
	# @var EWSType_BodyTypeType
	#
	self.BodyType=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : '_',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'BodyType',
		'required' : False,
		'type' : 'BodyTypeType',
		},
		]
# end this->schema
# end function __construct()
# end class BodyType
