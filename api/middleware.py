from django.utils.deprecation import MiddlewareMixin

class AuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        user_id = request.COOKIES.get('user_id')
        if user_id and not request.session.get('user_id'):
            request.session['user_id'] = user_id

