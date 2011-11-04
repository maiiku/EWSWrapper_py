##
# Definition of the NonEmptyArrayOfAttendeesType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the NonEmptyArrayOfAttendeesType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_NonEmptyArrayOfAttendeesType (EWSType):
	##
	# Attendee property
	#
	# @var EWSType_AttendeeType
	#
	self.Attendee=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'Attendee',
		'required' : False,
		'type' : 'AttendeeType',
		},
		]
# end this->schema
# end function __construct()
# end class NonEmptyArrayOfAttendeesType
