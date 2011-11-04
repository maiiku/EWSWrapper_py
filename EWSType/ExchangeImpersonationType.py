##
# Definition of the ExchangeImpersonationType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the ExchangeImpersonationType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_ExchangeImpersonationType (EWSType):
	##
	# ConnectingSID property
	#
	# @var EWSType_ConnectingSIDType
	#
	self.ConnectingSID=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'ConnectingSID',
		'required' : False,
		'type' : 'ConnectingSIDType',
		},
		]
# end this->schema
# end function __construct()
# end class ExchangeImpersonationType
