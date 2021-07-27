import requests
import user_variables as var
def AddProduct(url, product_id, product_name):
    url = url+"/"+product_id
    r = requests.post(url, json = {"id": product_id, "productname": product_name})
    return r

r = AddProduct(var.getURL(), "12345", "Solar Panel")
print(r.status_code)

