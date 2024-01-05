from django.core.paginator import Paginator
from django.shortcuts import render
from operations import Email, AuthenticationUser
from bs4 import BeautifulSoup
from io import BytesIO
import base64, zipfile, uuid

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

def compress_files(files):
    buffer = BytesIO()
    result = []
    zip_filename = f'file_archive_{uuid.uuid4().hex}.zip'
    with zipfile.ZipFile(buffer, 'w') as zip_file:
        for index, file in enumerate(files, start=1):
            original_filename = file.name
            entry_name = f'{original_filename}'
            zip_file.writestr(entry_name, file.read())
            result.append({
                "name_file": zip_filename,
                "base_64": None
            })
    compressed_data = buffer.getvalue()
    for item in result:
        item["base_64"] = base64.b64encode(compressed_data).decode("utf-8")
    return result


def remove_html_tags(input_string):
    soup = BeautifulSoup(input_string, 'html.parser')
    return soup.get_text()

def Composer(request):
	if request.method == 'POST':
		_data = request.POST.copy()
		_data['sender'] = request.session['pk_employee']
		_data['receives'] = [int(i) for i in request.POST.getlist('receives')]
		_data['message'] = remove_html_tags(request.POST.get('message', ''))
		_data['subject'] = _data['subject'] if _data['subject'] != '' else "Sin asunto"
		compressed_files = compress_files(request.FILES.getlist('file'))
		_data['file'] = compressed_files[0]
		if not Email(request).Create_Email(_data)['result']:
			pass
	return render(request,'email/compose.html', {'emails':AuthenticationUser(request).Get_List_Email()})

def Details_Email(request, pk):
	return render(request,'email/email-detail.html',{'email': Email(request).Get_Email(pk)})