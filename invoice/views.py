from operations import Invoice, Customer, Inventory, Setting
from from_number_to_letters import Thousands_Separator
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
import json, requests, env

def Get_List_Invoice(request,type_document):
	data = Invoice(request).Get_List_Invoice(type_document)
	items_per_page = 20
	paginator = Paginator(data, items_per_page)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request,'invoice/list_invoice.html', {'page_obj': page_obj} )

def Annulled_Invoice(request):
	if request.is_ajax():
		return HttpResponse(Invoice(request).Annulled_Invoice())

def View_Invoice(request, pk):
	data = Invoice(request).Get_Invoice(pk)
	subtotal = 0
	tax = 0
	ipo = 0
	discount = 0
	for i in data['details']:
		subtotal += float(i['price']) * float(i['quantity'])
		tax += float(i['tax']) * float(i['quantity'])
		ipo += float(i['ipo']) * float(i['quantity'])
		discount += float(i['discount']) * float(i['quantity'])

	total = subtotal + tax + ipo
	print(total)
	return render(request,'invoice/invoice.html',{'data':data, 'sub':subtotal, 'tax': tax, 'totals': total, 'ipo':ipo, 'discount': discount})

def Get_Number(request):
	if request.is_ajax():
		return HttpResponse(Setting(request).Get_Resolution({"type_document": request.GET['type_document'], "pk_branch": request.session['pk_branch']}))

def Return_Products(request):
	if request.is_ajax():
		Inventory(request).Return_Products()
		return HttpResponse(True)

def Return_Product_UNIQUE(request):
	if request.is_ajax():
		Inventory(request).Return_Product_UNIQUE()
		return HttpResponse(True)

def Create_Invoice(request):
	if request.is_ajax():
		return HttpResponse(Inventory(request).Product_Reserved())
	Inventory(request).Return_Products()
	return render(request,'invoice/order.html',{
		'client':Customer(request).Get_List_Customer(),
		'product':Inventory(request).Get_List_Products()
	})

def Loading_Product(request):
	if request.is_ajax():
		return HttpResponse(json.dumps(Inventory(request).Get_Product(request.GET['code'])))
	
def Save_Invoice(request):
	if request.is_ajax():
		print(request.POST)
		headers_json = json.loads(request.POST.get('headers'))
		details_invoice_json = json.loads(request.POST.get('details_invoice'))
		paymentform = paymentform = {
		    "paymentform": 1,
		    "paymentmethod": 10,
		    "due_date": headers_json['date']
		}
		if int(headers_json['paymentform']) == 2:
			paymentform = {
		        "paymentform": 2,
		        "paymentmethod": 30,
		        "due_date": headers_json['date_invoice_due']
		    }
		data = headers_json
		data['details'] = details_invoice_json
		data['payment_form'] = paymentform
		result = Invoice(request).Create_Invoice(data)
		print(result,'DATOOOOO')
		return HttpResponse(result)


def Print_Invoice(request,pk):
	payload = json.dumps({"pk_invoice": pk})
	headers= {'Content-Type':'application/json'}
	response = requests.request("GET", env.GET_INVOICE, headers=headers, data=payload)
	data = json.loads(response.text)
	subtotals = 0
	tax = 0
	ipo = 0
	discount = 0
	for i in data['details']:
		quantity = float(i['quantity'])
		subtotals += float(i['price'])
		tax += float(i['tax']) * quantity
		ipo += float(i['ipo']) * quantity
		discount += float(i['discount']) * quantity
	totals = {
		"subtotals":Thousands_Separator(subtotals),
		"tax":Thousands_Separator(tax),
		"ipo":Thousands_Separator(ipo),
		"discount":0,
		'totals': Thousands_Separator(subtotals + ipo + tax)
	}
	page_invoice = 'pos'
	if int(data['type_document']) == 2:
		page_invoice = 'elect'
	return render(request,f'invoice/pos.html',{
		'invoice':data,
		'details':data['details'],
		'paymentmethodinvoice':data['payment_form'],
		'totals':totals,
		'client':data['customer'],
		'company':data['branch'],
		'number':data['resolution']['_from'],
		'type_document':page_invoice,
	})