from django.shortcuts import HttpResponse
import json
from django.shortcuts import render_to_response
from django.template import loader

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