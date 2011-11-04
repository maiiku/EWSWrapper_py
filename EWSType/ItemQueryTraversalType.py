##
# Definition of the ItemQueryTraversalType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Types of sub-tree traversal for deletion and enumeration
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_ItemQueryTraversalType (EWSType):
	##
	# Consider only folders that are direct children of the parent folder(s) in
	# question
	#
	# @var string
	#
	self.SHALLOW='Shallow'
	##
	# Consider only those items that are soft deleted from the parent folders
	# specified
	#
	# @var string
	#
	self.SOFT_DELETED='SoftDeleted'
	##
	# Constructor
	#
	def __init__() :
# end function __construct()
# end class EWSType_ItemQueryTraversalType
