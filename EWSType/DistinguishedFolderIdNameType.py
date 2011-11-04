##
# Definition of the DistinguishedFolderIdNameType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# URIs for the distinguished folders accessible from a mailbox
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_DistinguishedFolderIdNameType (EWSType):
	##
	# Calendar folder
	#
	# @var string
	#
	self.CALENDAR='calendar'
	##
	# Contacts folder
	#
	# @var string
	#
	self.CONTACTS='contacts'
	##
	# Deleted Items folder (ie. trash)
	#
	# @var string
	#
	self.DELETED_ITEMS='deleteditems'
	##
	# Drafts folder
	#
	# @var string
	#
	self.DRAFTS='drafts'
	##
	# Inbox folder
	#
	# @var string
	#
	self.INBOX='inbox'
	##
	# Journal folder
	#
	# @var string
	#
	self.JOURNAL='journal'
	##
	# Notes folder
	#
	# @var string
	#
	self.NOTES='notes'
	##
	# Outbox folder
	#
	# @var string
	#
	self.OUTBOX='outbox'
	##
	# Sent Items folder
	#
	# @var string
	#
	self.SENT_ITEMS='sentitems'
	##
	# Tasks folder
	#
	# @var string
	#
	self.TASKS='tasks'
	##
	# Root of the message folders
	#
	# @var string
	#
	self.MESSAGE_FOLDER_ROOT='msgfolderroot'
	##
	# Root of the self.folders=''
	#
	# @var string
	#
	self.PUBLIC_FOLDERS_ROOT='publicfoldersroot'
	##
	# Root of the user's mailbox
	#
	# @var string
	#
	self.ROOT='root'
	##
	# Junk Email folder
	#
	# @var string
	#
	self.JUNK_EMAIL='junkemail'
	##
	# Search folders
	#
	# @var string
	#
	self.SEARCH_FOLDERS='searchfolders'
	##
	# Voicemail folder
	#
	# @var string
	#
	self.VOICEMAIL='voicemail'
	##
	# Constructor
	#
	def __init__() :
# end function __construct()
# end class EWSType_DistinguishedFolderIdNameType
