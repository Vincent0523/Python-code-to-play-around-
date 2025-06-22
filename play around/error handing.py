import requests

try:
    num  =int(input("Enter number: "))
except ValueError:
    print("That wasn't a number!")
else:
    print("It was a number")


#custom headers + error handling
try:
    headers = {"title": "the name of the title"}
    respons = requests.get("the url", headers=headers)
    respons.raise_for_statuse()#raise error for bad status
    print(respons.json())
except requests.exceptions.RequestException as e:
    print("Error:",e)
