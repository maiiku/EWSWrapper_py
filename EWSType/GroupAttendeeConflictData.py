##
# Definition of the GroupAttendeeConflictData type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the GroupAttendeeConflictData type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_GroupAttendeeConflictData (EWSType):
	##
	# NumberOfMembers property
	#
	# @var EWSType_int
	#
	self.NumberOfMembers=''
	##
	# NumberOfMembersAvailable property
	#
	# @var EWSType_int
	#
	self.NumberOfMembersAvailable=''
	##
	# NumberOfMembersWithConflict property
	#
	# @var EWSType_int
	#
	self.NumberOfMembersWithConflict=''
	##
	# NumberOfMembersWithNoData property
	#
	# @var EWSType_int
	#
	self.NumberOfMembersWithNoData=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'NumberOfMembers',
		'required' : False,
		'type' : 'int',
		},
		{'name' : 'NumberOfMembersAvailable',
		'required' : False,
		'type' : 'int',
		},
		{'name' : 'NumberOfMembersWithConflict',
		'required' : False,
		'type' : 'int',
		},
		{'name' : 'NumberOfMembersWithNoData',
		'required' : False,
		'type' : 'int',
		},
		]
# end this->schema
# end function __construct()
# end class GroupAttendeeConflictData
