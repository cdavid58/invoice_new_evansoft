from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from operations import Supplier


def List_Supplier(request):
	data = Supplier(request).List_Supplier()
	items_per_page = 20
	paginator = Paginator(data, items_per_page)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request,'supplier/list_supplier.html', {'page_obj': page_obj})


def Create_Supplier(request):
	if request.is_ajax():
		return HttpResponse(Supplier(request).Create_Supplier())
	return render(request,'supplier/add.html')


def Delete_Supplier(request):
	if request.is_ajax():
		return HttpResponse(Supplier(request).Delete_Supplier())


def Edit_Supplier(request, pk):
	if request.is_ajax():
		data = request.GET.copy()
		for i in data.keys():
			if data[i] == "":
				data[i] = None
		data['pk_supplier'] = pk
		return HttpResponse(Supplier(request).Update_Supplier(data))
	return render(request,'supplier/edit.html',{'supplier':Supplier(request).Get_Supplier(pk)})
