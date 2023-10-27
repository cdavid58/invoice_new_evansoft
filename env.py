URL_LOCAL = "http://127.0.0.1:9090"
URL_SERVER = ""

URL_IN_USE = URL_LOCAL

#AUTHENTICATION 

LOGIN = f"{URL_IN_USE}/user/Login/"



#SUPPLIER

LIST_SUPPLIER = f"{URL_IN_USE}/inventory/List_Supplier/"
CREATE_SUPPLIER = f"{URL_IN_USE}/inventory/Create_Supplier/"
DELETE_SUPPLIER = f"{URL_IN_USE}/inventory/Delete_Supplier/"
GET_SUPPLIER = f"{URL_IN_USE}/inventory/Get_Supplier/"
UPDATE_SUPPLIER = f"{URL_IN_USE}/inventory/Update_Supplier/"




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




#INVOICE

GET_LIST_INVOICE = f"{URL_IN_USE}/invoice/Get_List_Invoice/"
ANNULLED_INVOICE = f"{URL_IN_USE}/invoice/Annulled_Invoice/"





