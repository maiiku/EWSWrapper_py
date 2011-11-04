##
# Definition of the IndividualAttendeeConflictData type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the IndividualAttendeeConflictData type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_IndividualAttendeeConflictData (EWSType):
	##
	# BusyType property
	#
	# @var EWSType_LegacyFreeBusyType
	#
	self.BusyType=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'BusyType',
		'required' : False,
		'type' : 'LegacyFreeBusyType',
		},
		]
# end this->schema
# end function __construct()
# end class IndividualAttendeeConflictData
