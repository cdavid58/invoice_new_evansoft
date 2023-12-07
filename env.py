URL_LOCAL = "http://127.0.0.1:9090"
URL_SERVER = ""

URL_APPLICATION = "http://localhost:8000"

URL_IN_USE = URL_LOCAL

#AUTHENTICATION 

LOGIN = f"{URL_IN_USE}/user/Login/"
GET_LIST_EMPLOYEE = f"{URL_IN_USE}/user/Get_List_Employee/"
LOGOUT = f"{URL_IN_USE}/user/LogOut/"
UPDATE_USER = f"{URL_IN_USE}/user/Update_User/"



#SUPPLIER

LIST_SUPPLIER = f"{URL_IN_USE}/inventory/List_Supplier/"
CREATE_SUPPLIER = f"{URL_IN_USE}/inventory/Create_Supplier/"
DELETE_SUPPLIER = f"{URL_IN_USE}/inventory/Delete_Supplier/"
GET_SUPPLIER = f"{URL_IN_USE}/inventory/Get_Supplier/"
UPDATE_SUPPLIER = f"{URL_IN_USE}/inventory/Update_Supplier/"

#EMPLOYEE

GET_EMPLOYEE = f"{URL_IN_USE}/user/Get_Employee/"

#INVENTORY

GET_LIST_PRODUCTS = f"{URL_IN_USE}/inventory/Get_List_Products/"
CREATE_PRODUCT = f"{URL_IN_USE}/inventory/Create_Product/"
DELETE_PRODUCT = f"{URL_IN_USE}/inventory/Delete_Product/"
GET_PRODUCT = f"{URL_IN_USE}/inventory/Get_Product/"
UPDATE_PRODUCT = f"{URL_IN_USE}/inventory/Update_Product/"
GET_LIST_PRODUCTS_SUPPLIER = f"{URL_IN_USE}/inventory/Get_List_Products_Supplier/"

GET_CATEGORY = f"{URL_IN_USE}/inventory/Get_Category/"
GET_SUBCATEGORY = f"{URL_IN_USE}/inventory/Get_SubCategory/"


#SHOPPING

VERIFIED_INVOICE = f"{URL_IN_USE}/shopping/Verified_Invoice/"
CREATE_SHOPPING = f"{URL_IN_USE}/shopping/Create_Shopping/"


#CUSTOMER

GET_LIST_CUSTOMER = f"{URL_IN_USE}/customer/Get_List_Customer/"
GET_CUSTOMER = f"{URL_IN_USE}/customer/Get_Customer/"
UPDATE_CUSTOMER = f"{URL_IN_USE}/customer/Update_Customer/"
CREATE_CUSTOMER = f"{URL_IN_USE}/customer/Create_Customer/"
DELETE_CLIENT = f"{URL_IN_USE}/customer/Delete_Client/"

#INVOICE

GET_LIST_INVOICE = f"{URL_IN_USE}/invoice/Get_List_Invoice/"
ANNULLED_INVOICE = f"{URL_IN_USE}/invoice/Annulled_Invoice/"
GET_INVOICE = f"{URL_IN_USE}/invoice/Get_Invoice/"



#SETTING
GET_TYPE_WORKER = f"{URL_IN_USE}/setting/Get_Type_Worker/"
GET_TYPE_CONTRACT = f"{URL_IN_USE}/setting/Get_Type_Contract/"
GET_TSUB_TYPE_WORKER = f"{URL_IN_USE}/setting/Get_TSub_Type_Worker/"
GET_PAYROLL_TYPE_DOCUMENT_IDENTIFICATION = f"{URL_IN_USE}/setting/Get_Payroll_Type_Document_Identification/"
GET_MUNICIPALITIES = f"{URL_IN_USE}/setting/Get_Municipalities/"
GET_PERMISSION = f"{URL_IN_USE}/setting/Get_Permission/"
GET_TYPE_DOCUMENT_I = f"{URL_IN_USE}/setting/Get_Type_Document_I/"
GET_TYPE_REGIMEN = f"{URL_IN_USE}/setting/Get_Type_Regimen/"
GET_TYPE_ORGANIZATION = f"{URL_IN_USE}/setting/Get_Type_Organization/"


