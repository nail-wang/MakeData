from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
import json
from Myapp.models import *

def get_tools(request):
    tools = DB_tool.objects.all()
    res = {}
    res['tools'] = list(tools.values())
    return HttpResponse(json.dumps(res),content_type='application/json')