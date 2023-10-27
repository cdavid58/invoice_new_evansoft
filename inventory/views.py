from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from operations import Inventory, Supplier

def Get_List_Products(request):
	data = Inventory(request).Get_List_Products()
	items_per_page = 20
	paginator = Paginator(data, items_per_page)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request,'inventory/list_inventory.html', {'page_obj': page_obj})


def Create_Product(request):
	if request.is_ajax():
		return HttpResponse(Inventory(request).Create_Product())
	return render(request,'inventory/add.html',{'cat': Inventory(request).Get_Category(), 'supplier':Supplier(request).List_Supplier()})

def Get_Subcategory(request):
	if request.is_ajax():
		return HttpResponse(Inventory(request).Get_List_SubCategory())

def Load_Inventory_Excel(request):
	if request.is_ajax():
		import json
		result = None
		for i in json.loads(request.POST['data']):
			for j in i:
				_data = j
				_data['pk_subcategory'] = 1
				_data['pk_supplier'] = 2
				request.GET = j
				result = Inventory(request).Create_Product(excel = 1)
		return HttpResponse(result)

def Delete_Product(request):
	if request.is_ajax():
		return HttpResponse(Inventory(request).Delete_Product())


def Edit_Product(request, code):
	if request.is_ajax():
		return HttpResponse(Inventory(request).Update_Product(request))
	return render(request,'inventory/edit.html',{'p':Inventory(request).Get_Product(code), 
					'cat': Inventory(request).Get_Category(),
					'supplier':Supplier(request).List_Supplier()
				})
