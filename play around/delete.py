import requests

url = "the name of the url"
respons = requests.delete(url)
print("Status:", respons.status_code)
print("Deleted:",respons.text)#it sbould be empty or success message