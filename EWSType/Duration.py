##
# Definition of the Duration type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the Duration type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_Duration (EWSType):
	##
	# StartTime property
	#
	# @var EWSType_dateTime
	#
	self.StartTime=''
	##
	# EndTime property
	#
	# @var EWSType_dateTime
	#
	self.EndTime=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'StartTime',
		'required' : False,
		'type' : 'dateTime',
		},
		{'name' : 'EndTime',
		'required' : False,
		'type' : 'dateTime',
		},
		]
# end this->schema
# end function __construct()
# end class Duration
