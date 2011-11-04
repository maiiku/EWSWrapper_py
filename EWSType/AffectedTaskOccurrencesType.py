##
# Definition of the IndexBasePointType type
#
# @author Michal Korzeniowski <mko_san@lafiel.net>
#
class EWSType_IndexBasePointType (EWSType):
	##
	# Specifies that a DeleteItem request deletes the master task, and therefore all recurring tasks that are associated with the master task.
	#
	# @var string
	#
	self.BEGINNING='Beginning'
	##
	# Specifies that a DeleteItem request deletes only the current occurrence of a task.
	#
	# @var string
	#
	self.END='End'
	##
	# Constructor
	#
	def __init__() :
# end function __construct()
# end class CalendarItemCreateOrDeleteOperationType
