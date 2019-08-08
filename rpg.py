#Xractz
#IndoSec

import json, re
from requests import Session
s = Session()

print("RESET PASSWORD IG by Xractz")
id = input("\nEnter your username/email/phone number: ")

url = "https://www.instagram.com/accounts/account_recovery_send_ajax/"

g = s.get("https://www.instagram.com/accounts/password/reset/").text
token = re.search(r'csrf_token":"(.*?)"',g).group(1)

headers = {
    'x-csrftoken': token
}

data = {
	'email_or_username':id
	,'recaptcha_challenge_field':''
}

r = s.post(url, data=data, headers=headers)
a = json.loads(r.text)
print(f"Status  : {a['status']}")
print(f"Message : {a['message']}")
