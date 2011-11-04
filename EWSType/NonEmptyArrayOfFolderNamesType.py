##
# Definition of the NonEmptyArrayOfFolderNamesType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the NonEmptyArrayOfFolderNamesType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_NonEmptyArrayOfFolderNamesType (EWSType):
	##
	# FolderName property
	#
	# @var string
	#
	self.FolderName=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'FolderName',
		'required' : False,
		'type' : 'string',
		},
		]
# end this->schema
# end function __construct()
# end class NonEmptyArrayOfFolderNamesType
