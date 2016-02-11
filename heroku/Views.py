from django.shortcuts import HttpResponse
import json
import logging
from django.template import loader
from heroku.models import userTable
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

logger = logging.getLogger('file')

def goToLogin(request):
    data = {}
    json_data = {}
    logger.debug("method invoked")
    print "method invoked"
    if request.method == "POST":
        data['request'] = 'request is POST'
        json_data = json.dumps(data)
    else:
        template = loader.get_template('login.html')
        return HttpResponse(template.render(json_data, request))
    return HttpResponse(json_data)


def authenticateUser(request):
    return HttpResponse("You are authenticated")

@csrf_exempt
def createUser(request):
    try:
        print "Create user method invoked"
        print str(request)
        data = {}
        json_data = {}
        u = userTable(userName = request.POST.get('userName'),
        password = request.POST.get('password'),
        phone = request.POST.get('phone'),
        emailId = request.POST.get('email'))
        u.save()
    except:
        import traceback
        print traceback.format_exc()
    #template = loader.get_template('login.html')
    return JsonResponse({'status': 'user created'})
    #return HttpResponse(json.dumps({'status': 'user created'}), content_type="application/json")
