from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from operations import Customer, Setting
import env, json



def Get_List_Customer(request):
	data = Customer(request).Get_List_Customer()
	items_per_page = 20
	paginator = Paginator(data, items_per_page)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request,'client/list_client.html', {'page_obj': page_obj})

def Edit_Customer(request,pk):
	if request.is_ajax():
		data_str = request.GET.get('data', '{}')
		data = json.loads(data_str)
		data['pk_customer'] = pk
		return HttpResponse(Customer(request).Update_Customer(data))
	s = Setting(request)
	return render(request,'client/edit.html',{
		'data':Customer(request).Get_Customer(pk),
		'Get_Type_Regimen': s.Get_Data(env.GET_TYPE_REGIMEN),
		'Get_Type_Organization': s.Get_Data(env.GET_TYPE_ORGANIZATION),
		'Get_Type_Document_I': s.Get_Data(env.GET_TYPE_DOCUMENT_I),
		'municipalities': s.Get_Data(env.GET_MUNICIPALITIES)
		})

def Delete_Client(request):
	if request.is_ajax():
		return HttpResponse(Customer(request).Delete_Client())

def Create_Customer(request):
	if request.is_ajax():
		data_str = request.GET.get('data', '{}')
		data = json.loads(data_str)
		data['pk_employee'] = request.session['pk_employee']
		return HttpResponse(Customer(request).Create_Customer(data))
	s = Setting(request)
	return render(request,'client/add.html',{
		'Get_Type_Regimen': s.Get_Data(env.GET_TYPE_REGIMEN),
		'Get_Type_Organization': s.Get_Data(env.GET_TYPE_ORGANIZATION),
		'Get_Type_Document_I': s.Get_Data(env.GET_TYPE_DOCUMENT_I),
		'municipalities': s.Get_Data(env.GET_MUNICIPALITIES)
	})