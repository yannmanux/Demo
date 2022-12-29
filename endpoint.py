import requests 

url = input('enter the url : ')
if url[0:7] == ('https://'):
    print('proceed')
else:
    print('enter a good url')
    exit(2)

url_end_point = requests.get(f'{url}')
code = url_end_point.status_code
if code == 200:
    print ('success'),
else :
   print('wrong endpoint')