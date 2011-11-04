##
# Definition of the AlternateIdBaseType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the AlternateIdBaseType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_AlternateIdBaseType (EWSType):
	##
	# Format property
	#
	# @var EWSType_IdFormatType
	#
	self.Format=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'Format',
		'required' : False,
		'type' : 'IdFormatType',
		},
		]
# end this->schema
# end function __construct()
# end class AlternateIdBaseType
