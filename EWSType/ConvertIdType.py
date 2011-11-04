##
# Definition of the ConvertIdType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the ConvertIdType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_ConvertIdType (EWSType):
	##
	# SourceIds property
	#
	# @var EWSType_NonEmptyArrayOfAlternateIdsType
	#
	self.SourceIds=''
	##
	# DestinationFormat property
	#
	# @var EWSType_IdFormatType
	#
	self.DestinationFormat=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'SourceIds',
		'required' : False,
		'type' : 'NonEmptyArrayOfAlternateIdsType',
		},
		{'name' : 'DestinationFormat',
		'required' : False,
		'type' : 'IdFormatType',
		},
		]
# end this->schema
# end function __construct()
# end class ConvertIdType
