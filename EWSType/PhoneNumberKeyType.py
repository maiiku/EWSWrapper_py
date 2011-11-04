##
# Definition of the PhoneNumberKeyType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Phone number key type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_PhoneNumberKeyType (EWSType):
	##
	# Phone number key for assistant phone number
	#
	# @var string
	#
	self.ASSISTANT_PHONE='AssistantPhone'
	##
	# Phone number key for business fax number
	#
	# @var string
	#
	self.BUSINESS_FAX='BusinessFax'
	##
	# Phone number key for business phone number
	#
	# @var string
	#
	self.BUSINESS_PHONE='BusinessPhone'
	##
	# Phone number key for second business phone number
	#
	# @var string
	#
	self.BUSINESS_PHONE_2='BusinessPhone2'
	##
	# Phone number key for callback
	#
	# @var string
	#
	self.CALLBACK='Callback'
	##
	# Phone number key for car phone
	#
	# @var string
	#
	self.CAR_PHONE='CarPhone'
	##
	# Phone number key for company main phone
	#
	# @var string
	#
	self.COMPANY_MAIN_PHONE='CompanyMainPhone'
	##
	# Phone number key for home fax number
	#
	# @var string
	#
	self.HOME_FAX='HomeFax'
	##
	# Phone number key for home phone number
	#
	# @var string
	#
	self.HOME_PHONE='HomePhone'
	##
	# Phone number key for second home phone number
	#
	# @var string
	#
	self.HOME_PHONE_2='HomePhone2'
	##
	# Phone number key for ISDN line
	#
	# @var string
	#
	self.ISDN='Isdn'
	##
	# Phone number key for mobile phone number
	#
	# @var string
	#
	self.MOBILE_PHONE='MobilePhone'
	##
	# Phone number key for other fax number
	#
	# @var string
	#
	self.OTHER_FAX='OtherFax'
	##
	# Phone number key for other phone number
	#
	# @var string
	#
	self.OTHER_PHONE='OtherTelephone'
	##
	# Phone number key for pager
	#
	# @var string
	#
	self.PAGER='Pager'
	##
	# Phone number key for primary phone number
	#
	# @var string
	#
	self.PRIMARY_PHONE='PrimaryPhone'
	##
	# Phone number key for radio phone number
	#
	# @var string
	#
	self.RADIO_PHONE='RadioPhone'
	##
	# Phone number key for telex
	#
	# @var string
	#
	self.TELEX='Telex'
	##
	# Phone number key for TTY TTD phone number
	#
	# @var string
	#
	self.TTY_TTD_PHONE='TtyTtdPhone'
	##
	# Value of the desired mapping. Should be one of the constants from the
	# EWSType_PhoneNumberKeyType class.
	#
	# @var string
	#
	self._=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : '_',
		'required' : True,
		'type' : 'string',
		},
		]
# end this->schema
# end function __construct()
	##
	# Returns the value of this object as a string
	#
	# @return string
	#
	def __toString() :
		return self._
# end function __toString()
# end class EWSType_PhoneNumberKeyType
