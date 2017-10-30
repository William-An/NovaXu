import requests
import config
cookies_string = config.cookies_string
nova_url = config.nova_url
cookies = dict([(k,g) for k,g in [j.split('=') for j in [i for i in cookies_string.split(';')]]])
res = requests.post(nova_url, cookies=cookies)
while res.status_code != 200:
	res = requests.post(nova_url, cookies=cookies).json()
print(res.json()['msg'])