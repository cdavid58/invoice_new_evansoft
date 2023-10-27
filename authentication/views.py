from operations import AuthenticationUser
from django.http import HttpResponse
from django.shortcuts import render

def Login(request):
	if request.is_ajax():
		return HttpResponse(AuthenticationUser(request).Login())
	return render(request,'authentication/login.html')