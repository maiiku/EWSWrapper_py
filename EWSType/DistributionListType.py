##
# Definition of the DistributionListType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the DistributionListType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_DistributionListType (EWSType):
	##
	# DisplayName property
	#
	# @var string
	#
	self.DisplayName=''
	##
	# FileAs property
	#
	# @var string
	#
	self.FileAs=''
	##
	# ContactSource property
	#
	# @var EWSType_ContactSourceType
	#
	self.ContactSource=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'DisplayName',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'FileAs',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'ContactSource',
		'required' : False,
		'type' : 'ContactSourceType',
		},
		]
# end this->schema
# end function __construct()
# end class DistributionListType
