##
# Definition of the Suggestion type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the Suggestion type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_Suggestion (EWSType):
	##
	# MeetingTime property
	#
	# @var EWSType_dateTime
	#
	self.MeetingTime=''
	##
	# IsWorkTime property
	#
	# @var EWSType_boolean
	#
	self.IsWorkTime=''
	##
	# SuggestionQuality property
	#
	# @var EWSType_SuggestionQuality
	#
	self.SuggestionQuality=''
	##
	# AttendeeConflictDataArray property
	#
	# @var EWSType_ArrayOfAttendeeConflictData
	#
	self.AttendeeConflictDataArray=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'MeetingTime',
		'required' : False,
		'type' : 'dateTime',
		},
		{'name' : 'IsWorkTime',
		'required' : False,
		'type' : 'boolean',
		},
		{'name' : 'SuggestionQuality',
		'required' : False,
		'type' : 'SuggestionQuality',
		},
		{'name' : 'AttendeeConflictDataArray',
		'required' : False,
		'type' : 'ArrayOfAttendeeConflictData',
		},
		]
# end this->schema
# end function __construct()
# end class Suggestion
