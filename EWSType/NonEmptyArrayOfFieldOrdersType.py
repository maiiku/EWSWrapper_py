##
# Definition of the NonEmptyArrayOfFieldOrdersType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the NonEmptyArrayOfFieldOrdersType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_NonEmptyArrayOfFieldOrdersType (EWSType):
	##
	# FieldOrder property
	#
	# @var EWSType_FieldOrderType
	#
	self.FieldOrder=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'FieldOrder',
		'required' : False,
		'type' : 'FieldOrderType',
		},
		]
# end this->schema
# end function __construct()
# end class NonEmptyArrayOfFieldOrdersType
