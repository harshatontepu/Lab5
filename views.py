from django.shortcuts import render
from django.http import HttpResponse
import json
def index(request):
	data={ 'Message':'Hello World! This is Harsha, Ok bye'}
	return HttpResponse(json.dumps(data),content_type="application/json")
