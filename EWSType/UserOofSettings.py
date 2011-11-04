##
# Definition of the UserOofSettings type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
##
# Definition of the UserOofSettings type
#
# @author James I. Armes <http:
#www.jamesarmes.net>
#
class EWSType_UserOofSettings (EWSType):
	##
	# OofState property
	#
	# @var EWSType_OofState
	#
	self.OofState=''
	##
	# ExternalAudience property
	#
	# @var EWSType_ExternalAudience
	#
	self.ExternalAudience=''
	##
	# Duration property
	#
	# @var EWSType_Duration
	#
	self.Duration=''
	##
	# InternalReply property
	#
	# @var EWSType_ReplyBody
	#
	self.InternalReply=''
	##
	# ExternalReply property
	#
	# @var EWSType_ReplyBody
	#
	self.ExternalReply=''
	##
	# Constructor
	#
	def __init__() :
		self.schema = [{'name' : 'OofState',
		'required' : False,
		'type' : 'OofState',
		},
		{'name' : 'ExternalAudience',
		'required' : False,
		'type' : 'ExternalAudience',
		},
		{'name' : 'Duration',
		'required' : False,
		'type' : 'Duration',
		},
		{'name' : 'InternalReply',
		'required' : False,
		'type' : 'ReplyBody',
		},
		{'name' : 'ExternalReply',
		'required' : False,
		'type' : 'ReplyBody',
		},
		]
# end this->schema
# end function __construct()
# end class UserOofSettings
