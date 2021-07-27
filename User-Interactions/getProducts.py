#python code for hexal application(UI-API-Lambda-DynamoDB)
import user_variables as var
import requests
import ast

def GetCompleteListOfProducts(url):
    response = requests.get(url)
    elements = response.json().items()
    
    statusCode = response.status_code
    for key, value in elements:
        if key == "body":
            products = value
            break
    return products,statusCode

#products = [{"id":"12345","productname":"Solar Panel"},{"id":"12346","productname":"LED Lights"},{"id":"12348","productname":"Water Pumps"},{"id":"12347","productname":"Generator"}]
products, statusCode = GetCompleteListOfProducts(var.getURL())
products = ast.literal_eval(products)
for ele in products:
    print(ele["id"], ele["productname"], "\n")
