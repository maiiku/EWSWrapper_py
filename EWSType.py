'''
/* EWSWrapper_py
 * ====================================================
 * @author Michal Korzeniowski <mko_san@lafiel.net>
 * @version 0.1
 * @date 10-2011
 * @website http://ewswrapper.lafiel.net/
 * ====================================================
 * Desciption
 * Provides enumerable types from Exchange Web Services
 * for EWSWrapper. Accessible from EWSWrapper under
 * self.types
 * 
 * ==================================================*/
'''
class EWSType:


    class EWSType_AffectedTaskOccurrencesType:
	##
	# Specifies that a DeleteItem request deletes the master task, and therefore all recurring tasks that are associated with the master task.
	#
	# @var string
	#
	ALL_OCCURRENCES='AllOccurrences'
	##
	# Specifies that a DeleteItem request deletes only the current occurrence of a task.
	#
	# @var string
	#
	SPECIFIED_OCCURRENCES_ONLY='SpecifiedOccurrenceOnly'
	##
	# Constructor
	#
	def __init__() :
	    pass
    # end class CalendarItemCreateOrDeleteOperationType


    class EWSType_BodyTypeResponseType:
	##
	# All properties are retured in the response
	#
	# @var string
	#
	BEST='Best'
	##
	# Default properties are returned in the respoonse
	#
	# @var string
	#
	HTML='HTML'
	##
	# Plain text body
	#
	# @var string
	#
	TEXT='Text'
	##
	# Constructor
	#
	def __init__() :
	    pass
    # end class EWSType_BodyTypeResponseType


    class EWSType_CalendarItemCreateOrDeleteOperationType:
	##
	# Send to
	#
	# @var string
	#
	SEND_TO_NONE='SendToNone'
	##
	# Send to
	#
	# @var string
	#
	SEND_ONLY_TO_ALL='SendOnlyToAll'
	##
	# Send to
	#
	# @var string
	#
	SEND_TO_ALL_AND_SAVE_COPY='SendToAllAndSaveCopy'
	##
	# Constructor
	#
	def __init__() :
	    pass
    # end class CalendarItemCreateOrDeleteOperationType

    
    class EWSType_CalendarItemUpdateOperationType:
	##
	# Send to
	#
	# @var string
	#
	SEND_TO_NONE='SendToNone'
	##
	# Send to
	#
	# @var string
	#
	SEND_ONLY_TO_ALL='SendOnlyToAll'
	##
	# Send to
	#
	# @var string
	#
	SEND_TO_ALL_AND_SAVE_COPY='SendToAllAndSaveCopy'
	##
	# Send to
	#
	# @var string
	#
	SEND_ONLY_TO_CHANGED='SendOnlyToChanged'
	##
	# Send to
	#
	# @var string
	#
	SEND_TO_CHANGED_AND_SAVE_COPY='SendToChangedAndSaveCopy'
	##
	# Constructor
	#
	def __init__() :
	    pass
    # end class CalendarItemUpdateOperationType
 
    
    class EWSType_DefaultShapeNamesType:
	##
	# All properties are retured in the response
	#
	# @var string
	#
	ALL_PROPERTIES='AllProperties'
	##
	# Default properties are returned in the respoonse
	#
	# @var string
	#
	DEFAULT_PROPERTIES='Default'
	##
	# Only folder ids are returned in the response
	#
	# @var string
	#
	ID_ONLY='IdOnly'
	##
	# Constructor
	#
	def __init__() :
	    pass
    # end class EWSType_DefaultShapeNamesType
	    

    class EWSType_DistinguishedFolderIdNameType:
	##
	# Calendar folder
	#
	# @var string
	#
	CALENDAR='calendar'
	##
	# Contacts folder
	#
	# @var string
	#
	CONTACTS='contacts'
	##
	# Deleted Items folder (ie. trash)
	#
	# @var string
	#
	DELETED_ITEMS='deleteditems'
	##
	# Drafts folder
	#
	# @var string
	#
	DRAFTS='drafts'
	##
	# Inbox folder
	#
	# @var string
	#
	INBOX='inbox'
	##
	# Journal folder
	#
	# @var string
	#
	JOURNAL='journal'
	##
	# Notes folder
	#
	# @var string
	#
	NOTES='notes'
	##
	# Outbox folder
	#
	# @var string
	#
	OUTBOX='outbox'
	##
	# Sent Items folder
	#
	# @var string
	#
	SENT_ITEMS='sentitems'
	##
	# Tasks folder
	#
	# @var string
	#
	TASKS='tasks'
	##
	# Root of the message folders
	#
	# @var string
	#
	MESSAGE_FOLDER_ROOT='msgfolderroot'
	##
	# Root of the folders=''
	#
	# @var string
	#
	PUBLIC_FOLDERS_ROOT='publicfoldersroot'
	##
	# Root of the user's mailbox
	#
	# @var string
	#
	ROOT='root'
	##
	# Junk Email folder
	#
	# @var string
	#
	JUNK_EMAIL='junkemail'
	##
	# Search folders
	#
	# @var string
	#
	SEARCH_FOLDERS='searchfolders'
	##
	# Voicemail folder
	#
	# @var string
	#
	VOICEMAIL='voicemail'
	##
	# Constructor
	#
	def __init__() :
	    pass
    # end class EWSType_DistinguishedFolderIdNameType

    class EWSType_DisposalType:
	##
	# Deletes the item irrevocably. Does not move the item to the Deleted Items
	# Folder.
	#
	# @var string
	#
	HARD_DELETE='HardDelete'
	##
	# Does not actually delete the item, but instead simply moves it to the
	# Deleted Items folder.
	#
	# @var string
	#
	MOVE_TO_DELETED_ITEMS='MoveToDeletedItems'
	##
	# "Deletes" the item so that it is no longer visible in the folder, but
	# actually still exists there. Avoid using this because there is nothing
	# that you can do with soft-deleted items from EWS aside from finding them.
	#
	# @var string
	#
	SOFT_DELETE='SoftDelete'
	##
	# Constructor
	#
	def __init__() :
	    pass
    # end class EWSType_DisposalType


    class EWSType_IndexBasePointType:
	##
	# Specifies that a DeleteItem request deletes the master task, and therefore all recurring tasks that are associated with the master task.
	#
	# @var string
	#
	BEGINNING='Beginning'
	##
	# Specifies that a DeleteItem request deletes only the current occurrence of a task.
	#
	# @var string
	#
	END='End'
	##
	# Constructor
	#
	def __init__() :
	    pass
    # end class CalendarItemCreateOrDeleteOperationType
   
    
    class EWSType_ItemQueryTraversalType:
	##
	# Consider only folders that are direct children of the parent folder(s) in
	# question
	#
	# @var string
	#
	SHALLOW='Shallow'
	##
	# Consider only those items that are soft deleted from the parent folders
	# specified
	#
	# @var string
	#
	SOFT_DELETED='SoftDeleted'
	##
	# Constructor
	#
	def __init__() :
	    pass
    # end class EWSType_ItemQueryTraversalType

    
    class EWSType_FolderQueryTraversalType:
	##
	# Consider both direct children as well as all subfolders contained within
	# those children as well as the children's children, etc.
	#
	# @var string
	#
	DEEP='Deep'
	##
	# Consider only folders that are direct children of the parent folder(s) in
	# question
	#
	# @var string
	#
	SHALLOW='Shallow'
	##
	# Consider only those items that are soft deleted from the parent folders
	# specified
	#
	# @var string
	#
	SOFT_DELETED='SoftDeleted'
	##
	# Constructor
	#
	def __init__() :
	    pass
    # end class EWSType_FolderQueryTraversalType
    
    
    class EWSType_FileAsMappingType:
	##
	# File as mapping for "company"
	#
	# @var string
	#
	COMPANY='Company'
	##
	# File as mapping for "last name, first name"
	#
	# @var
	#
	COMPANY_LAST_COMMA_FIRST='CompanyLastCommaFirst'
	##
	# File as mapping for "company last name first name"
	#
	# @var string
	#
	COMPANY_LAST_FIRST='CompanyLastFirst'
	##
	# File as mapping for "company last name first name"
	#
	# @var string
	#
	COMPANY_LAST_SPACE_FIRST='CompanyLastSpaceFirst'
	##
	# File as mapping for "first name last name"
	#
	# @var string
	#
	FIRST_SPACE_LAST='FirstSpaceLast'
	##
	# File as mapping for "last name first name"
	#
	# @var string
	#
	LAST_FIRST='LastFirst'
	##
	# File as mapping for "last name first name company"
	#
	# @var string
	#
	LAST_FIRST_COMPANY='LastFirstCompany'
	##
	# File as mapping for "last name first name suffix"
	#
	# @var string
	#
	LAST_FIRST_SUFFIX='LastFirstSuffix'
	##
	# File as mapping for "last name, first name"
	#
	# @var string
	#
	LAST_COMMA_FIRST='LastCommaFirst'
	##
	# File as mapping for "last name, first name company"
	#
	# @var string
	#
	LAST_COMMA_FIRST_COMPANY='LastCommaFirstCompany'
	##
	# File as mapping for "last name first name"
	#
	# @var string
	#
	LAST_SPACE_FIRST='LastSpaceFirst'
	##
	# File as mapping for "lasy name first name company"
	#
	# @var string
	#
	LAST_SPACE_FIRST_COMPANY='LastSpaceFirstCompany'
	##
	# File as mapping to use when no mapping is desired.
	#
	# @var string
	#
	NONE='None'
	##
	# Constructor
	#
	def __init__() :
	    pass
    # end class EWSType_FileAsMappingType
    
    
    class EWSType_EmailAddressKeyType:
	##
	# Key for a contacts first email address
	#
	# @var string
	#
	EMAIL_ADDRESS_1='EmailAddress1'
	##
	# Key for a contacts second email address
	#
	# @var string
	#
	EMAIL_ADDRESS_2='EmailAddress2'
	##
	# Key for a contacts third email address
	#
	# @var string
	#
	EMAIL_ADDRESS_3='EmailAddress3'
	##
	# Constructor
	#
	def __init__() :
	    pass
    # end class EWSType_EmailAddressKeyType
    
    
    class EWSType_PhysicalAddressKeyType:
	##
	# Business physical address type
	#
	# @var string
	#
	BUSINESS='Business'
	##
	# Home physical address type
	#
	# @var string
	#
	HOME='Home'
	##
	# Other physical address type
	#
	# @var string
	#
	OTHER='Other'
	##
	# Constructor
	#
	def __init__() :
	    pass
    # end class EWSType_PhysicalAddressKeyType
    
        
    class EWSType_PhoneNumberKeyType:
	##
	# Phone number key for assistant phone number
	#
	# @var string
	#
	ASSISTANT_PHONE='AssistantPhone'
	##
	# Phone number key for business fax number
	#
	# @var string
	#
	BUSINESS_FAX='BusinessFax'
	##
	# Phone number key for business phone number
	#
	# @var string
	#
	BUSINESS_PHONE='BusinessPhone'
	##
	# Phone number key for second business phone number
	#
	# @var string
	#
	BUSINESS_PHONE_2='BusinessPhone2'
	##
	# Phone number key for callback
	#
	# @var string
	#
	CALLBACK='Callback'
	##
	# Phone number key for car phone
	#
	# @var string
	#
	CAR_PHONE='CarPhone'
	##
	# Phone number key for company main phone
	#
	# @var string
	#
	COMPANY_MAIN_PHONE='CompanyMainPhone'
	##
	# Phone number key for home fax number
	#
	# @var string
	#
	HOME_FAX='HomeFax'
	##
	# Phone number key for home phone number
	#
	# @var string
	#
	HOME_PHONE='HomePhone'
	##
	# Phone number key for second home phone number
	#
	# @var string
	#
	HOME_PHONE_2='HomePhone2'
	##
	# Phone number key for ISDN line
	#
	# @var string
	#
	ISDN='Isdn'
	##
	# Phone number key for mobile phone number
	#
	# @var string
	#
	MOBILE_PHONE='MobilePhone'
	##
	# Phone number key for other fax number
	#
	# @var string
	#
	OTHER_FAX='OtherFax'
	##
	# Phone number key for other phone number
	#
	# @var string
	#
	OTHER_PHONE='OtherTelephone'
	##
	# Phone number key for pager
	#
	# @var string
	#
	PAGER='Pager'
	##
	# Phone number key for primary phone number
	#
	# @var string
	#
	PRIMARY_PHONE='PrimaryPhone'
	##
	# Phone number key for radio phone number
	#
	# @var string
	#
	RADIO_PHONE='RadioPhone'
	##
	# Phone number key for telex
	#
	# @var string
	#
	TELEX='Telex'
	##
	# Phone number key for TTY TTD phone number
	#
	# @var string
	#
	TTY_TTD_PHONE='TtyTtdPhone'
	##
	# Constructor
	#
	def __init__() :
	    pass
    # end class EWSType_PhoneNumberKeyType
    
    
    class EWSType_ImportanceChoicesType:
	##
	# Specifies low priority
	#
	# @var string
	#
	LOW='Low'
	##
	# Specifies normal priority
	#
	# @var string
	#
	NORMAL='Normal'
	##
	# Specifies high priority
	#
	# @var string
	#
	HIGH='High'
	##
	# Constructor
	#
	def __init__() :
	    pass
    # end class EWSType_ImportanceChoicesType

    
    class EWSType_TaskStatusType:
	    ##
	    # Specifies that the task is completed.
	    #
	    # @var string
	    #
	    COMPLETED='Completed'
	    ##
	    # Specifies that the task is deferred.
	    #
	    # @var string
	    #
	    DEFERRED='Deferred'
	    ##
	    # Specifies that the task is in progress.
	    #
	    # @var string
	    #
	    INPROGRESS='InProgress'
	    ##
	    # Specifies that the task is in progress.
	    #
	    # @var string
	    #
	    NOTSTARTED='NotStarted'
	    ##
	    # Specifies that the task is in progress.
	    #
	    # @var string
	    #
	    WAITINGONOTHERS='WaitingOnOthers'
	    ##
	    # Constructor
	    #
	    def __init__() :
		pass
    # end class EWSType_TaskStatusType
    
    
    class EWSType_SortDirectionType:
	##
	# Items are sorted in ascending order
	#
	# @var string
	#
	ASCENDING='Ascending'
	##
	# Items are sorted in descending order
	#
	# @var string
	#
	DESCENDING='Descending'
	##
	# Constructor
	#
	def __init__() :
	    pass
    # end class EWSType_SortDirectionType
    
    
    class EWSType_SensitivityChoicesType:
	##
	# Specifies normal confidentiality.
	#
	# @var string
	#
	NORMAL='Normal'
	##
	# Specifies personal confidentiality.
	#
	# @var string
	#
	PERSONAL='Personal'
	##
	# Specifies confidentiality.=''
	#
	# @var string
	#
	PRIVATESENSITIVITY='Private'
	##
	# Specifies confidential confidentiality.
	#
	# @var string
	#
	CONFIDENTIAL='Confidential'
	##
	# Constructor
	#
	def __init__() :
	    pass
    # end class EWSType_SensitivityChoicesType
    
    
    
    class EWSType_MessageDispositionType:
	##
	# When used in the CreateItemType, the e-mail message item is saved in the folder that is specified by the SavedItemFolderId property, or in the Sent Items folder if SavedItemFolderId is not specified.
	#
	# @var string
	#
	SAVEONLY='SaveOnly'
	##
	# When used in the CreateItemType, the e-mail message item is sent and a copy is saved in the folder that is specified by the SavedItemFolderId property, or in the Sent Items folder if SavedItemFolderId is not specified.
	#
	# @var string
	#
	SENDANDSAVECOPY='SendAndSaveCopy'
	##
	#When used in the CreateItemType, the e-mail message item is sent but no copy is saved.
	#
	# @var string
	#
	SENDONLY='SendOnly'
	##
	# Constructor
	#
	def __init__() :
	    pass
    # end class EWSType_MessageDispositionType	

	
    class EWSType_ConflictResolutionType:
	##
	# If there is a conflict, the UpdateItem operation will overwrite information.
	#
	# @var string
	#
	ALWAYSOVERWRITE='AlwaysOverwrite'
	##
	# The UpdateItem operation automatically resolves any conflict. The AutoResolve option will in most cases overwrite the existing value for a property. In some cases, the new value is ignored and the original value is retained. For example, user A changes the Sensitivity property from Normal to Confidential. Then user B sets the value to Public. In this example, the Confidential setting is retained and user B's update is ignored.
	#
	# @var string
	#
	AUTORESOLVE='AutoResolve'
	##
	# If conflict exists, the UpdateItem operation fails and an error is returned.
	# @var string
	#
	NEVEROVERWRITE='NeverOverwrite'
	##
	# Constructor
	#
	def __init__() :
	    pass
    # end class EWSType_MessageDispositionType	
    
   
    ##
    # Definition of the CalendarItemType type
    class EWSType_CalendarItemType:
    
	    def __init__(self, subject, start, end, body=None, location=None):
		##
		# UID property
		#
		# @var string
		#
		self.UID=''
		##
		# RecurrenceId property
		#
		# @var EWSType_dateTime
		#
		self.RecurrenceId=''
		##
		# DateTimeStamp property
		#
		# @var EWSType_dateTime
		#
		self.DateTimeStamp=''
		##
		# Start property
		#
		# @var EWSType_dateTime
		#
		self.Start=''
		##
		# End property
		#
		# @var EWSType_dateTime
		#
		self.End=''
		##
		# OriginalStart property
		#
		# @var EWSType_dateTime
		#
		self.OriginalStart=''
		##
		# IsAllDayEvent property
		#
		# @var EWSType_boolean
		#
		self.IsAllDayEvent=''
		##
		# LegacyFreeBusyStatus property
		#
		# @var EWSType_LegacyFreeBusyType
		#
		self.LegacyFreeBusyStatus=''
		##
		# Location property
		#
		# @var string
		#
		self.Location=''
		##
		# When property
		#
		# @var string
		#
		self.When=''
		##
		# IsMeeting property
		#
		# @var EWSType_boolean
		#
		self.IsMeeting=''
		##
		# IsCancelled property
		#
		# @var EWSType_boolean
		#
		self.IsCancelled=''
		##
		# IsRecurring property
		#
		# @var EWSType_boolean
		#
		self.IsRecurring=''
		##
		# MeetingRequestWasSent property
		#
		# @var EWSType_boolean
		#
		self.MeetingRequestWasSent=''
		##
		# IsResponseRequested property
		#
		# @var EWSType_boolean
		#
		self.IsResponseRequested=''
		##
		# CalendarItemType property
		#
		# @var EWSType_CalendarItemTypeType
		#
		self.CalendarItemType=''
		##
		# MyResponseType property
		#
		# @var EWSType_ResponseTypeType
		#
		self.MyResponseType=''
		##
		# Organizer property
		#
		# @var EWSType_SingleRecipientType
		#
		self.Organizer=''
		##
		# RequiredAttendees property
		#
		# @var EWSType_NonEmptyArrayOfAttendeesType
		#
		self.RequiredAttendees=''
		##
		# OptionalAttendees property
		#
		# @var EWSType_NonEmptyArrayOfAttendeesType
		#
		self.OptionalAttendees=''
		##
		# Resources property
		#
		# @var EWSType_NonEmptyArrayOfAttendeesType
		#
		self.Resources=''
		##
		# ConflictingMeetingCount property
		#
		# @var EWSType_int
		#
		self.ConflictingMeetingCount=''
		##
		# AdjacentMeetingCount property
		#
		# @var EWSType_int
		#
		self.AdjacentMeetingCount=''
		##
		# ConflictingMeetings property
		#
		# @var EWSType_NonEmptyArrayOfAllItemsType
		#
		self.ConflictingMeetings=''
		##
		# AdjacentMeetings property
		#
		# @var EWSType_NonEmptyArrayOfAllItemsType
		#
		self.AdjacentMeetings=''
		##
		# Duration property
		#
		# @var string
		#
		self.Duration=''
		##
		# TimeZone property
		#
		# @var string
		#
		self.TimeZone=''
		##
		# AppointmentReplyTime property
		#
		# @var EWSType_dateTime
		#
		self.AppointmentReplyTime=''
		##
		# AppointmentSequenceNumber property
		#
		# @var EWSType_int
		#
		self.AppointmentSequenceNumber=''
		##
		# AppointmentState property
		#
		# @var EWSType_int
		#
		self.AppointmentState=''
		##
		# Recurrence property
		#
		# @var EWSType_RecurrenceType
		#
		self.Recurrence=''
		##
		# FirstOccurrence property
		#
		# @var EWSType_OccurrenceInfoType
		#
		self.FirstOccurrence=''
		##
		# LastOccurrence property
		#
		# @var EWSType_OccurrenceInfoType
		#
		self.LastOccurrence=''
		##
		# ModifiedOccurrences property
		#
		# @var EWSType_NonEmptyArrayOfOccurrenceInfoType
		#
		self.ModifiedOccurrences=''
		##
		# DeletedOccurrences property
		#
		# @var EWSType_NonEmptyArrayOfDeletedOccurrencesType
		#
		self.DeletedOccurrences=''
		##
		# MeetingTimeZone property
		#
		# @var EWSType_TimeZoneType
		#
		self.MeetingTimeZone=''
		##
		# ConferenceType property
		#
		# @var EWSType_int
		#
		self.ConferenceType=''
		##
		# AllowNewTimeProposal property
		#
		# @var EWSType_boolean
		#
		self.AllowNewTimeProposal=''
		##
		# IsOnlineMeeting property
		#
		# @var EWSType_boolean
		#
		self.IsOnlineMeeting=''
		##
		# MeetingWorkspaceUrl property
		#
		# @var string
		#
		self.MeetingWorkspaceUrl=''
		##
		# NetShowUrl property
		#
		# @var string
		#
		self.NetShowUrl=''
		
		
		self.Subject = subject
		self.Start = start
		self.End = end
		self.Body = body
		self.Location = location
		#self.hasreminder = hasreminder
    
	    def __str__(self):
		return '''Subject: %s
Start: %s
End: %s
Location: %s
Body: %s''' % (self.subject, self.start, self.end, self.location, self.body)


