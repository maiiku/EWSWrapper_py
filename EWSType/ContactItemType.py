##
# Definition of the ContactItemType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the ContactItemType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_ContactItemType (EWSType):
	##
	# FileAs property
	#
	# @var string
	#
	self.FileAs=''
	##
	# FileAsMapping property
	#
	# @var EWSType_FileAsMappingType
	#
	self.FileAsMapping=''
	##
	# DisplayName property
	#
	# @var string
	#
	self.DisplayName=''
	##
	# GivenName property
	#
	# @var string
	#
	self.GivenName=''
	##
	# Initials property
	#
	# @var string
	#
	self.Initials=''
	##
	# MiddleName property
	#
	# @var string
	#
	self.MiddleName=''
	##
	# Nickname property
	#
	# @var string
	#
	self.Nickname=''
	##
	# CompleteName property
	#
	# @var EWSType_CompleteNameType
	#
	self.CompleteName=''
	##
	# CompanyName property
	#
	# @var string
	#
	self.CompanyName=''
	##
	# EmailAddresses property
	#
	# @var EWSType_EmailAddressDictionaryType
	#
	self.EmailAddresses=''
	##
	# PhysicalAddresses property
	#
	# @var EWSType_PhysicalAddressDictionaryType
	#
	self.PhysicalAddresses=''
	##
	# PhoneNumbers property
	#
	# @var EWSType_PhoneNumberDictionaryType
	#
	self.PhoneNumbers=''
	##
	# AssistantName property
	#
	# @var string
	#
	self.AssistantName=''
	##
	# Birthday property
	#
	# @var EWSType_dateTime
	#
	self.Birthday=''
	##
	# BusinessHomePage property
	#
	# @var EWSType_anyURI
	#
	self.BusinessHomePage=''
	##
	# Children property
	#
	# @var EWSType_ArrayOfStringsType
	#
	self.Children=''
	##
	# Companies property
	#
	# @var EWSType_ArrayOfStringsType
	#
	self.Companies=''
	##
	# ContactSource property
	#
	# @var EWSType_ContactSourceType
	#
	self.ContactSource=''
	##
	# Department property
	#
	# @var string
	#
	self.Department=''
	##
	# Generation property
	#
	# @var string
	#
	self.Generation=''
	##
	# ImAddresses property
	#
	# @var EWSType_ImAddressDictionaryType
	#
	self.ImAddresses=''
	##
	# JobTitle property
	#
	# @var string
	#
	self.JobTitle=''
	##
	# Manager property
	#
	# @var string
	#
	self.Manager=''
	##
	# Mileage property
	#
	# @var string
	#
	self.Mileage=''
	##
	# OfficeLocation property
	#
	# @var string
	#
	self.OfficeLocation=''
	##
	# PostalAddressIndex property
	#
	# @var EWSType_PhysicalAddressIndexType
	#
	self.PostalAddressIndex=''
	##
	# Profession property
	#
	# @var string
	#
	self.Profession=''
	##
	# SpouseName property
	#
	# @var string
	#
	self.SpouseName=''
	##
	# Surname property
	#
	# @var string
	#
	self.Surname=''
	##
	# WeddingAnniversary property
	#
	# @var EWSType_dateTime
	#
	self.WeddingAnniversary=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'FileAs',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'FileAsMapping',
		'required' : False,
		'type' : 'FileAsMappingType',
		},
		{'name' : 'DisplayName',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'GivenName',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'Initials',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'MiddleName',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'Nickname',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'CompleteName',
		'required' : False,
		'type' : 'CompleteNameType',
		},
		{'name' : 'CompanyName',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'EmailAddresses',
		'required' : False,
		'type' : 'EmailAddressDictionaryType',
		},
		{'name' : 'PhysicalAddresses',
		'required' : False,
		'type' : 'PhysicalAddressDictionaryType',
		},
		{'name' : 'PhoneNumbers',
		'required' : False,
		'type' : 'PhoneNumberDictionaryType',
		},
		{'name' : 'AssistantName',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'Birthday',
		'required' : False,
		'type' : 'dateTime',
		},
		{'name' : 'BusinessHomePage',
		'required' : False,
		'type' : 'anyURI',
		},
		{'name' : 'Children',
		'required' : False,
		'type' : 'ArrayOfStringsType',
		},
		{'name' : 'Companies',
		'required' : False,
		'type' : 'ArrayOfStringsType',
		},
		{'name' : 'ContactSource',
		'required' : False,
		'type' : 'ContactSourceType',
		},
		{'name' : 'Department',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'Generation',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'ImAddresses',
		'required' : False,
		'type' : 'ImAddressDictionaryType',
		},
		{'name' : 'JobTitle',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'Manager',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'Mileage',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'OfficeLocation',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'PostalAddressIndex',
		'required' : False,
		'type' : 'PhysicalAddressIndexType',
		},
		{'name' : 'Profession',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'SpouseName',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'Surname',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'WeddingAnniversary',
		'required' : False,
		'type' : 'dateTime',
		},
		]
# end this->schema
# end function __construct()
# end class ContactItemType
