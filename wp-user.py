import requests,sys
try:
	url=sys.argv[1]+'/wp-json/wp/v2/users/'
except:
	print('\n EX : python2 wp-user.py http://google.com\n')
	sys.exit()
try:
	r=requests.get(url)
except:
	print('[-] Error ..')
	sys.exit()
j = r.json()
print('\n# => @knassar702')
for i in j:
	print('----------------')
	print('[*] Name : {}\n[*] ID   : {}\n[*] User : {}'.format(i['name'],i['id'],i['slug']))
print('----------------\n')
# Coded By : Khaled Nassar @knassar702
