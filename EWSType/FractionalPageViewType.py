##
# Definition of the FractionalPageViewType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the FractionalPageViewType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_FractionalPageViewType (EWSType):
	##
	# Numerator property
	#
	# @var EWSType_int
	#
	self.Numerator=''
	##
	# Denominator property
	#
	# @var EWSType_int
	#
	self.Denominator=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'Numerator',
		'required' : False,
		'type' : 'int',
		},
		{'name' : 'Denominator',
		'required' : False,
		'type' : 'int',
		},
		]
# end this->schema
# end function __construct()
# end class FractionalPageViewType
