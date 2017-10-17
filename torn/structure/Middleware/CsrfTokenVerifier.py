from torn.app import Middleware

# Inherits the parent class Middleware
# Includes constructor, handle and excpeturls
class CsrfTokenVerifier(Middleware):

	# Let's handle the request
	def handle(self, request, next):
		if(self.in_exceptions()):
			return next(request)

		# TODO