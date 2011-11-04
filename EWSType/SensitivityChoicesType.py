##
# Definition of the SensitivityChoicesType type
#
# @author Michal Korzeniowski <mko_san@lafiel.net>
#
class EWSType_SensitivityChoicesType (EWSType):
	##
	# Specifies normal confidentiality.
	#
	# @var string
	#
	self.NORMAL='Normal'
	##
	# Specifies personal confidentiality.
	#
	# @var string
	#
	self.PERSONAL='Personal'
	##
	# Specifies self.confidentiality.=''
	#
	# @var string
	#
	self.PRIVATESENSITIVITY='Private'
	##
	# Specifies confidential confidentiality.
	#
	# @var string
	#
	self.CONFIDENTIAL='Confidential'
	##
	# Constructor
	#
	def __init__() :
# end function __construct()
# end class EWSType_SensitivityChoicesType
