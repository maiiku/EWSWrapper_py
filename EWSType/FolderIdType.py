##
# Definition of the FolderIdType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the FolderIdType type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_FolderIdType (EWSType):
	##
	# Id property
	#
	# @var string
	#
	self.Id=''
	##
	# ChangeKey property
	#
	# @var string
	#
	self.ChangeKey=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'Id',
		'required' : False,
		'type' : 'string',
		},
		{'name' : 'ChangeKey',
		'required' : False,
		'type' : 'string',
		},
		]
# end this->schema
# end function __construct()
# end class FolderIdType
