import env, json, requests

class AuthenticationUser:
	def __init__(self,request):
		self.headers = {'Content-Type': 'application/json'}
		self.request = request

	def Login(self):
		values = None
		try:
			payload = json.dumps(self.request.GET)
			response = requests.request("POST", env.LOGIN, headers=self.headers, data=payload)
			values = json.loads(response.text)
			self.request.session['pk_employee'] = values['pk_employee']
			self.request.session['name_employee'] = values['name']
			self.request.session['pk_branch'] = values['pk_branch']
			self.request.session['name_branch'] = values['name_branch']
			self.request.session['logo'] = values['logo']
			self.request.session['permission'] = values['permission']
		except Exception as e:
			print("Error")
		return json.dumps({'result': values['result'], 'message': values['message']})

class Supplier:
	def __init__(self,request):
		self.headers = {'Content-Type': 'application/json'}
		self.request = request

	def List_Supplier(self):
		payload = json.dumps({"pk_employee":self.request.session['pk_employee']})
		response = requests.request("GET", env.LIST_SUPPLIER, headers= self.headers, data=payload)
		return json.loads(response.text)

	def Create_Supplier(self):
		data = self.request.GET.copy()
		for i in data.keys():
			if data[i] == "":
				data[i] = None
		data['pk_employee'] = self.request.session['pk_employee']
		payload = json.dumps(data)
		response = requests.request("POST", env.CREATE_SUPPLIER, headers= self.headers, data=payload)
		return json.dumps(json.loads(response.text))

	def Delete_Supplier(self):
		data = self.request.GET.copy()
		data['pk_employee'] = self.request.session['pk_employee']
		payload = json.dumps(data)
		response = requests.request("POST", env.DELETE_SUPPLIER, headers= self.headers, data=payload)
		return json.dumps(json.loads(response.text))

	def Get_Supplier(self, pk):
		response = requests.request("GET", env.GET_SUPPLIER, headers= self.headers, data=json.dumps({'pk_supplier':pk}))
		return json.loads(response.text)

	def Update_Supplier(self, data):
		response = requests.request("PUT", env.UPDATE_SUPPLIER, headers= self.headers, data=json.dumps(data))
		return json.dumps(json.loads(response.text))

class Inventory:
	def __init__(self,request):
		self.headers = {'Content-Type': 'application/json'}
		self.request = request

	def Get_List_Products(self):
		response = requests.request("GET", env.GET_LIST_PRODUCTS, headers= self.headers, data=json.dumps({'pk_employee':self.request.session['pk_employee']}))
		return json.loads(response.text)

	def Create_Product(self, excel = 0):
		data = self.request.GET.copy()
		for i in data.keys():
			if data[i] == "":
				return json.dumps({'result':False, 'message':"No puede dejar ningun campo vacio"})
		data['pk_employee'] = self.request.session['pk_employee']
		data['excel'] = excel
		response = requests.request("POST", env.CREATE_PRODUCT, headers= self.headers, data=json.dumps(data))
		return json.dumps(json.loads(response.text))

	def Get_Category(self):
		response = requests.request("GET", env.GET_CATEGORY, headers= self.headers, data={})
		return json.loads(response.text)

	def Get_List_SubCategory(self):
		response = requests.request("POST", env.GET_SUBCATEGORY, headers= self.headers, data=json.dumps(self.request.GET))
		return json.dumps(json.loads(response.text))

	def Delete_Product(self):
		data = self.request.GET.copy()
		data['pk_employee'] = self.request.session['pk_employee']
		response = requests.request("DELETE", env.DELETE_PRODUCT, headers= self.headers, data=json.dumps(data))
		return json.dumps(json.loads(response.text))

	def Get_Product(self,code):
		payload = json.dumps({
		  "pk_employee": self.request.session['pk_employee'],
		  "code": code
		})
		response = requests.request("GET", env.GET_PRODUCT, headers= self.headers, data=payload)
		return json.loads(response.text)

	def Update_Product(self,data):
		data = self.request.GET.copy()
		data['pk_employee'] = self.request.session['pk_employee']
		payload = json.dumps(data)
		response = requests.request("PUT", env.UPDATE_PRODUCT, headers= self.headers, data=payload)
		print(response.text)
		return json.dumps(json.loads(response.text))

	def Get_List_Products_Supplier(self):
		data = self.request.GET.copy()
		data['pk_employee'] = self.request.session['pk_employee']
		payload = json.dumps(data)
		response = requests.request("GET", env.GET_LIST_PRODUCTS_SUPPLIER, headers= self.headers, data=payload)
		return json.dumps(json.loads(response.text))

class Shopping:
	def __init__(self,request):
		self.headers = {'Content-Type': 'application/json'}
		self.request = request

	def Verified_Invoice(self):
		data = self.request.GET.copy()
		data['pk_employee'] = self.request.session['pk_employee']
		payload = json.dumps(data)
		response = requests.request("GET", env.VERIFIED_INVOICE, headers= self.headers, data=payload)
		return json.dumps(json.loads(response.text))

	def Save_Shopping(self, data):
		data['pk_employee'] = self.request.session['pk_employee']
		payload = json.dumps(data)
		response = requests.request("POST", env.CREATE_SHOPPING, headers= self.headers, data=payload)
		return json.dumps(json.loads(response.text))

class Invoice:
	def __init__(self,request):
		self.headers = {'Content-Type': 'application/json'}
		self.request = request

	def Get_List_Invoice(self,type_invoice):
		payload = json.dumps({
			'pk_employee':self.request.session['pk_employee'],
			'type_document': int(type_invoice)
		})
		response = requests.request("GET", env.GET_LIST_INVOICE, headers= self.headers, data=payload)
		print(json.loads(response.text))
		return json.loads(response.text)

	def Annulled_Invoice(self):
		data = self.request.GET.copy()
		data['pk_employee'] = self.request.session['pk_employee']
		response = requests.request("POST", env.ANNULLED_INVOICE, headers= self.headers, data=json.dumps(data))
		return json.dumps(json.loads(response.text))






