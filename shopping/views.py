from django.http import HttpResponse
from django.shortcuts import render
from operations import Inventory, Supplier, Shopping

def Register_Purchase(request):
	return render(request,'shopping/add.html',{'list_supplier':Supplier(request).List_Supplier()})

def Get_List_Products_Supplier(request):
	if request.is_ajax():
		return HttpResponse(Inventory(request).Get_List_Products_Supplier())

def Verified_Invoice(request):
	if request.is_ajax():
		return HttpResponse(Shopping(request).Verified_Invoice())

def Save_Shopping(request):
	if request.is_ajax():
		import json
		_data = request.POST
		data = json.loads(_data['headers'])
		data['details'] = json.loads(_data['items'])
		print(data)
		data['payment_form'] = {
			"pk_paymentform": 1 if int(data['pk_paymentform']) == 1 else 2,
			"pk_paymentmethod":10 if int(data['pk_paymentform']) == 1 else 30,
			"payment_due_date": json.loads(_data['headers'])['payment_due_date']
		}
		return HttpResponse(Shopping(request).Save_Shopping(data))