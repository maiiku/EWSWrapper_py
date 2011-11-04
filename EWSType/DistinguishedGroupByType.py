##
# Definition of the DistinguishedGroupByType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the DistinguishedGroupByType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_DistinguishedGroupByType (EWSType):
	##
	# StandardGroupBy property
	#
	# @var EWSType_StandardGroupByType
	#
	self.StandardGroupBy=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'StandardGroupBy',
		'required' : False,
		'type' : 'StandardGroupByType',
		},
		]
# end this->schema
# end function __construct()
# end class DistinguishedGroupByType
