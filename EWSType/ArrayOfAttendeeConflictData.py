##
# Definition of the ArrayOfAttendeeConflictData type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the ArrayOfAttendeeConflictData type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_ArrayOfAttendeeConflictData (EWSType):
	##
	# UnknownAttendeeConflictData property
	#
	# @var EWSType_UnknownAttendeeConflictData
	#
	self.UnknownAttendeeConflictData=''
	##
	# IndividualAttendeeConflictData property
	#
	# @var EWSType_IndividualAttendeeConflictData
	#
	self.IndividualAttendeeConflictData=''
	##
	# TooBigGroupAttendeeConflictData property
	#
	# @var EWSType_TooBigGroupAttendeeConflictData
	#
	self.TooBigGroupAttendeeConflictData=''
	##
	# GroupAttendeeConflictData property
	#
	# @var EWSType_GroupAttendeeConflictData
	#
	self.GroupAttendeeConflictData=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'UnknownAttendeeConflictData',
		'required' : False,
		'type' : 'UnknownAttendeeConflictData',
		},
		{'name' : 'IndividualAttendeeConflictData',
		'required' : False,
		'type' : 'IndividualAttendeeConflictData',
		},
		{'name' : 'TooBigGroupAttendeeConflictData',
		'required' : False,
		'type' : 'TooBigGroupAttendeeConflictData',
		},
		{'name' : 'GroupAttendeeConflictData',
		'required' : False,
		'type' : 'GroupAttendeeConflictData',
		},
		]
# end this->schema
# end function __construct()
# end class ArrayOfAttendeeConflictData
