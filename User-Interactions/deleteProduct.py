import user_variables as var
import requests

def UpdateProduct(url, product_id):
    url = url+"/"+product_id
    response = requests.delete(url, json = {"id": product_id})
    return response.status_code


statusCode = UpdateProduct(var.getURL(), "12345")
print(statusCode)