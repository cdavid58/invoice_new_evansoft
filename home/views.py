from django.shortcuts import render
from operations import Setting

def Index(request):
	return render(request,'index.html')

def Settings(request):
	data_company = Setting(request).Get_Branch()
	return render(request,'settings/company.html',{'branch':data_company, 'r':Setting(request).Get_Resolution_List()})