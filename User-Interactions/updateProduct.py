import user_variables as var
import requests

def UpdateProduct(url, product_id, updatedName):
    url = url+"/"+product_id
    response = requests.patch(url, json = {"id": product_id, "productname": updatedName})
    return response.status_code


statusCode = UpdateProduct(var.getURL(), "12345", "Solar Roof")
print(statusCode)