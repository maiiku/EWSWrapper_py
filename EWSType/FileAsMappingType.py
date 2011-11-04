##
# Definition of the FileAsMappingType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Mapping types for Contacts
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_FileAsMappingType (EWSType):
	##
	# File as mapping for "company"
	#
	# @var string
	#
	self.COMPANY='Company'
	##
	# File as mapping for "last name, first name"
	#
	# @var
	#
	self.COMPANY_LAST_COMMA_FIRST='CompanyLastCommaFirst'
	##
	# File as mapping for "company last name first name"
	#
	# @var string
	#
	self.COMPANY_LAST_FIRST='CompanyLastFirst'
	##
	# File as mapping for "company last name first name"
	#
	# @var string
	#
	self.COMPANY_LAST_SPACE_FIRST='CompanyLastSpaceFirst'
	##
	# File as mapping for "first name last name"
	#
	# @var string
	#
	self.FIRST_SPACE_LAST='FirstSpaceLast'
	##
	# File as mapping for "last name first name"
	#
	# @var string
	#
	self.LAST_FIRST='LastFirst'
	##
	# File as mapping for "last name first name company"
	#
	# @var string
	#
	self.LAST_FIRST_COMPANY='LastFirstCompany'
	##
	# File as mapping for "last name first name suffix"
	#
	# @var string
	#
	self.LAST_FIRST_SUFFIX='LastFirstSuffix'
	##
	# File as mapping for "last name, first name"
	#
	# @var string
	#
	self.LAST_COMMA_FIRST='LastCommaFirst'
	##
	# File as mapping for "last name, first name company"
	#
	# @var string
	#
	self.LAST_COMMA_FIRST_COMPANY='LastCommaFirstCompany'
	##
	# File as mapping for "last name first name"
	#
	# @var string
	#
	self.LAST_SPACE_FIRST='LastSpaceFirst'
	##
	# File as mapping for "lasy name first name company"
	#
	# @var string
	#
	self.LAST_SPACE_FIRST_COMPANY='LastSpaceFirstCompany'
	##
	# File as mapping to use when no mapping is desired.
	#
	# @var string
	#
	self.NONE='None'
	##
	# Value of the desired mapping. Should be one of the constants from the
	# EWSType_FileAsMappingType class.
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
# end class EWSType_FileAsMappingType
