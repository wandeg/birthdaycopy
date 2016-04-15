import requests

from config import FB_KEY

base_url = "https://graph.facebook.com/v2.6/me"

payload = {
	'fields':'id,name,friends{birthday,first_name,middle_name,last_name}',
	'access_token':FB_KEY
}

r = requests.get(base_url, params=payload)
