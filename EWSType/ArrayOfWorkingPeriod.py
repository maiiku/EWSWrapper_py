##
# Definition of the ArrayOfWorkingPeriod type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the ArrayOfWorkingPeriod type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_ArrayOfWorkingPeriod (EWSType):
	##
	# WorkingPeriod property
	#
	# @var EWSType_WorkingPeriod
	#
	self.WorkingPeriod=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'WorkingPeriod',
		'required' : False,
		'type' : 'WorkingPeriod',
		},
		]
# end this->schema
# end function __construct()
# end class ArrayOfWorkingPeriod
