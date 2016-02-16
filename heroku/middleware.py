
import datetime
import json

from django.template import loader
from django.http import HttpResponse

class SessionMiddleware(object):
    """
    Middleware to validate session
    """
    def process_request(self, request):
        try:
            url = str(request.META.get('PATH_INFO'))
            print(url)
            if url != '/' and url != '/login/' and url != '/authenticateUser/' and url != '/createUser/' and url != '/LoginScreen.js/':
                if request.session.get('isloggedin', '') != '1':
                    result = {'status': 'error', 'msg': 'Invalid Session.'}
                    return HttpResponse(json.dumps(result), content_type = "application/json")
        except:
            pass