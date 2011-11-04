##
# Definition of the TaskType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the TaskType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_TaskType (EWSType):
	##
	# ActualWork property
	#
	# @var EWSType_int
	#
	self.ActualWork=''
	##
	# AssignedTime property
	#
	# @var EWSType_dateTime
	#
	self.AssignedTime=''
	##
	# BillingInformation property
	#
	# @var string
	#
	self.BillingInformation=''
	##
	# ChangeCount property
	#
	# @var EWSType_int
	#
	self.ChangeCount=''
	##
	# Companies property
	#
	# @var EWSType_ArrayOfStringsType
	#
	self.Companies=''
	##
	# CompleteDate property
	#
	# @var EWSType_dateTime
	#
	self.CompleteDate=''
	##
	# Contacts property
	#
	# @var EWSType_ArrayOfStringsType
	#
	self.Contacts=''
	##
	# DelegationState property
	#
	# @var EWSType_TaskDelegateStateType
	#
	self.DelegationState=''
	##
	# Delegator property
	#
	# @var string
	#
	self.Delegator=''
	##
	# DueDate property
	#
	# @var EWSType_dateTime
	#
	self.DueDate=''
	##
	# IsAssignmentEditable property
	#
	# @var EWSType_int
	#
	self.IsAssignmentEditable=''
	##
	# IsComplete property
	#
	# @var EWSType_boolean
	#
	self.IsComplete=''
	##
	# IsRecurring property
	#
	# @var EWSType_boolean
	#
	self.IsRecurring=''
	##
	# IsTeamTask property
	#
	# @var EWSType_boolean
	#
	self.IsTeamTask=''
	##
	# Mileage property
	#
	# @var string
	#
	self.Mileage=''
	##
	# Owner property
	#
	# @var string
	#
	self.Owner=''
	##
	# PercentComplete property
	#
	# @var EWSType_double
	#
	self.PercentComplete=''
	##
	# Recurrence property
	#
	# @var EWSType_TaskRecurrenceType
	#
	self.Recurrence=''
	##
	# StartDate property
	#
	# @var EWSType_dateTime
	#
	self.StartDate=''
	##
	# Status property
	#
	# @var EWSType_TaskStatusType
	#
	self.Status=''
	##
	# StatusDescription property
	#
	# @var string
	#
	self.StatusDescription=''
	##
	# TotalWork property
	#
	# @var EWSType_int
	#
	self.TotalWork=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'ActualWork',
		'required' : False,
		'type' : 'int',
		},
		{'name' : 'AssignedTime',
		'required' : False,
		'type' : 'dateTime',
		},
		{'name' : 'BillingInformation',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'ChangeCount',
		'required' : False,
		'type' : 'int',
		},
		{'name' : 'Companies',
		'required' : False,
		'type' : 'ArrayOfStringsType',
		},
		{'name' : 'CompleteDate',
		'required' : False,
		'type' : 'dateTime',
		},
		{'name' : 'Contacts',
		'required' : False,
		'type' : 'ArrayOfStringsType',
		},
		{'name' : 'DelegationState',
		'required' : False,
		'type' : 'TaskDelegateStateType',
		},
		{'name' : 'Delegator',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'DueDate',
		'required' : False,
		'type' : 'dateTime',
		},
		{'name' : 'IsAssignmentEditable',
		'required' : False,
		'type' : 'int',
		},
		{'name' : 'IsComplete',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'IsRecurring',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'IsTeamTask',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'Mileage',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'Owner',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'PercentComplete',
		'required' : False,
		'type' : 'double',
		},
		{'name' : 'Recurrence',
		'required' : False,
		'type' : 'TaskRecurrenceType',
		},
		{'name' : 'StartDate',
		'required' : False,
		'type' : 'dateTime',
		},
		{'name' : 'Status',
		'required' : False,
		'type' : 'TaskStatusType',
		},
		{'name' : 'StatusDescription',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'TotalWork',
		'required' : False,
		'type' : 'int',
		},
		]
# end this->schema
# end function __construct()
# end class TaskType
