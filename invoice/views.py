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