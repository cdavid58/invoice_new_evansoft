from django.core.paginator import Paginator
from django.shortcuts import render
from operations import Email

def Inbox(request):
	data = Email(request).Get_List_Emals()
	items_per_page = 20
	paginator = Paginator(data, items_per_page)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request,'email/inbox.html', {'page_obj': page_obj} )

def Sender(request):
	data = Email(request).Get_List_Email_Sender()
	items_per_page = 20
	paginator = Paginator(data, items_per_page)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request,'email/inbox.html', {'page_obj': page_obj} )

def Composer(request):
	return render(request,'email/compose.html')