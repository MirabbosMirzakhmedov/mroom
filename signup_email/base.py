


# import requests
#
# url = "https://api.bigmailer.io/v1/me"
#
# querystring = {"limit":"10"}
#
# headers = {
#     "Accept": "application/json",
#     "X-API-Key": "a9e33e23-3cb5-4f4d-ba66-37c4107649f4"
# }
#
# response = requests.request("GET", url, headers=headers, params=querystring)
#
# print(response.text)


# TODO: Sending an email
import requests

brand_id = "32b13c73-42a5-4106-bb24-95140fc91463"
campaign_id = "4bd76469-f1ae-4ba0-9fb1-b5c94b0bbac7"
api_key = "a9e33e23-3cb5-4f4d-ba66-37c4107649f4"

url = f"https://api.bigmailer.io/v1/brands/{brand_id}/transactional-campaigns/{campaign_id}/send"

payload = {
    "email": "mirabbos.dov@gmail.com"
}
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "X-API-Key": api_key,
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)