from django.shortcuts import HttpResponse
import json
import logging
from django.template import loader
from heroku.models import userTable
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

logger = logging.getLogger('file')

def goToLogin(request):
    data = {}
    json_data = {}
    logger.debug("method invoked")
    if request.method == "POST":
        data['request'] = 'request is POST'
        json_data = json.dumps(data)
    else:
        template = loader.get_template('login.html')
        return HttpResponse(template.render(json_data, request))
    return HttpResponse(json_data)

@csrf_exempt
def authenticateUser(request):
    from django.contrib.auth import authenticate, login
    username = request.POST['loginUserName']
    password = request.POST['loginPassword']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            return HttpResponse("You are authenticated")
        else:
            return HttpResponse("Please enter valid credentials")
            # Return a 'disabled account' error message
    else:
        return HttpResponse("Please enter valid credentials")
        # Return an 'invalid login' error message.

@csrf_exempt
def createUser(request):
    try:
        # #print(request.session)
        # #print "Create user method invoked"
        # print str(request)
        # data = {}
        # json_data = {}
        u = userTable(userName = request.POST.get('userName'),
        password = request.POST.get('password'),
        phone = request.POST.get('phone'),
        emailId = request.POST.get('email'))
        u.save()
        user = User.objects.create_user(username=u.userName, email=u.emailId, password=u.password)
        user.save()
        print(user)
    except:
        import traceback
        print traceback.format_exc()
    #template = loader.get_template('login.html')
    return JsonResponse({'status': 'user created'})
    #return HttpResponse(json.dumps({'status': 'user create'}), content_type="application/json")
