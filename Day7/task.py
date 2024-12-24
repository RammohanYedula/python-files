import requests

responce = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

complete_details = responce.json()


for element in range(len(complete_details)):

    print(complete_details[element]["user"]["id"])