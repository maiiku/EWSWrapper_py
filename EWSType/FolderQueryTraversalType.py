##
# Definition of the FolderQueryTraversalType type
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
class EWSType_FolderQueryTraversalType (EWSType):
	##
	# Consider both direct children as well as all subfolders contained within
	# those children as well as the children's children, etc.
	#
	# @var string
	#
	self.DEEP='Deep'
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
# end class EWSType_FolderQueryTraversalType
