##
# Definition of the DisposalType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Types of deletion for items and folders
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_DisposalType (EWSType):
	##
	# Deletes the item irrevocably. Does not move the item to the Deleted Items
	# Folder.
	#
	# @var string
	#
	self.HARD_DELETE='HardDelete'
	##
	# Does not actually delete the item, but instead simply moves it to the
	# Deleted Items folder.
	#
	# @var string
	#
	self.MOVE_TO_DELETED_ITEMS='MoveToDeletedItems'
	##
	# "Deletes" the item so that it is no longer visible in the folder, but
	# actually still exists there. Avoid using this because there is nothing
	# that you can do with soft-deleted items from EWS aside from finding them.
	#
	# @var string
	#
	self.SOFT_DELETE='SoftDelete'
	##
	# Constructor
	#
	def __init__() :
# end function __construct()
# end class EWSType_DisposalType
