##
# Definition of the WorkingHours type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the WorkingHours type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_WorkingHours (EWSType):
	##
	# TimeZone property
	#
	# @var EWSType_SerializableTimeZone
	#
	self.TimeZone=''
	##
	# WorkingPeriodArray property
	#
	# @var EWSType_ArrayOfWorkingPeriod
	#
	self.WorkingPeriodArray=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'TimeZone',
		'required' : False,
		'type' : 'SerializableTimeZone',
		},
		{'name' : 'WorkingPeriodArray',
		'required' : False,
		'type' : 'ArrayOfWorkingPeriod',
		},
		]
# end this->schema
# end function __construct()
# end class WorkingHours
