from django.shortcuts import HttpResponse
import json
from django.shortcuts import render_to_response
from django.template import loader
from heroku.models import userTable

def goToLogin(request):
    data = {}
    json_data = {}

    if request.method == "POST":
        data['request'] = 'request is POST'
        json_data = json.dumps(data)
    else:
        template = loader.get_template('login.html')
        return HttpResponse(template.render(json_data, request))
    return HttpResponse(json_data)


def authenticateUser(request):
    return HttpResponse("You are authenticated")

def createUser(request):
    data = {}
    json_data = {}
    u = userTable(userName = request.POST.get('userName'),
    password = request.POST.get('password'),
    phone = request.POST.get('phone'),
    emailId = request.POST.get('email'))
    u.save()
    template = loader.get_template('login.html')
    data['statusCode'] = "0000"
    data['statusMessage'] = 'User Created Successfully'
    json_data = json.dumps(data)
    return HttpResponse(template.render(json_data, request))
    return HttpResponse("User created successfully", content_type="text/plain")