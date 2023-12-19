from django.core.paginator import Paginator
from django.http import HttpResponse
from operations import AuthenticationUser, Setting
from django.http import HttpResponse
from django.shortcuts import render
import json, env

def Login(request):
	if request.is_ajax():
		request.session['url_application'] = env.URL_APPLICATION
		return HttpResponse(AuthenticationUser(request).Login())
	return render(request,'authentication/login.html')

def LogOut(request):
	if request.is_ajax():
		if AuthenticationUser(request).LogOut()['result']:
			for i,j in list(request.session.items()):
				del request.session[i]
			return HttpResponse(json.dumps({'result':True}))
		return HttpResponse(json.dumps({'result':True}))



def List_Employee(request):
	data = AuthenticationUser(request).Get_List_User()
	items_per_page = 20
	paginator = Paginator(data, items_per_page)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request,'user/list_user.html', {'page_obj': page_obj})

def Create_Employee(request):
	s = Setting(request)
	if request.is_ajax():
		data_str = request.GET.get('data', '{}')
		data = json.loads(data_str)
		data['pk_employee'] = request.session['pk_employee']
		if "high_risk_pension" not in data:
			data['high_risk_pension'] = False
		if 'integral_salary' not in data:
			data['integral_salary'] = False
		return HttpResponse(AuthenticationUser(request).Create_Employee(data))
	return render(request,'user/add.html',{
		'type_worker': s.Get_Data(env.GET_TYPE_WORKER),
		'type_contract': s.Get_Data(env.GET_TYPE_CONTRACT),
		'sub_type_worker': s.Get_Data(env.GET_TSUB_TYPE_WORKER),
		'payroll_type_document_identification': s.Get_Data(env.GET_PAYROLL_TYPE_DOCUMENT_IDENTIFICATION),
		'municipalities': s.Get_Data(env.GET_MUNICIPALITIES)
		})

def Get_Employee(request,pk):
	s = Setting(request)
	employee = AuthenticationUser(request).Get_Employee(pk)
	request.session['pk_employee'] = employee['pk_employee']
	return render(request,'user/edit.html',{
			'data':employee,
			'type_worker': s.Get_Data(env.GET_TYPE_WORKER),
			'type_contract': s.Get_Data(env.GET_TYPE_CONTRACT),
			'sub_type_worker': s.Get_Data(env.GET_TSUB_TYPE_WORKER),
			'payroll_type_document_identification': s.Get_Data(env.GET_PAYROLL_TYPE_DOCUMENT_IDENTIFICATION),
			'municipalities': s.Get_Data(env.GET_MUNICIPALITIES),
			'list_permission': [ i['name_permission'] for i in employee['permission']],
			'permission':s.Get_Data(env.GET_PERMISSION)
		})


def Update_Data_Employee(request):
	if request.is_ajax():
		data_str = request.GET.get('data', '{}')
		data = json.loads(data_str)
		data['pk_employee'] = request.session['pk_employee']
		return HttpResponse(AuthenticationUser(request).Update_User(data))


def Delete_Employee(request):
	if request.is_ajax():
		return HttpResponse(AuthenticationUser(request).Delelete_User(request.GET))