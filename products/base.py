#TODO: Exercise 1: A proper request following all the previous instructions
# 1. Add variable type to the 'response'
# 2. Instead of using separate 'url' variable,
#    move 'https://amazon-products1.p.rapidapi.com/search' in .get(url=...)
# 3. Instead of using separate 'headers' variable,
#    move {... headers_content ...} in .get(headers=...)
# 4. Instead of using separate 'querystring' variable,
#    move {... querystring_content ...} in .get(params=...)
# 5. Choose one either single or double quotes,
#    and stick with them - replace all of them with one type.

import requests

response: requests.models.Response = requests.get(
    url="https://amazon-products1.p.rapidapi.com/search",
    headers={
        'x-rapidapi-key': "a8f0a072d2msh3d1bfc104318241p1aec10jsn70718bbf81a2",
        'x-rapidapi-host': "amazon-products1.p.rapidapi.com"
    },
    params={
        "country":"US","query":"MacBook+Pro"
    }
)

print(response.text)
