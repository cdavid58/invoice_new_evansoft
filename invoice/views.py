from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from operations import Invoice

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
		subtotal += float(i['cost']) * float(i['quantity'])
		tax += float(i['tax']) * float(i['quantity'])
		ipo += float(i['ipo']) * float(i['quantity'])
		discount += float(i['discount']) * float(i['quantity'])
	total = subtotal + tax + ipo
	return render(request,'invoice/invoice.html',{'data':data, 'sub':subtotal, 'tax': tax, 'totals': total, 'ipo':ipo, 'discount': discount})


def Create_Invoice(request):
	return render(request,'invoice/order.html')