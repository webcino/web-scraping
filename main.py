import requests 
from bs4 import BeautifulSoup as bs

github_user = input('input Github User: ')
url = 'https://github.com/'+github_user

r = requests.get(url)

soup = bs(r.content, 'html.parser')

profile_img = soup.find('img', {'class': 'avatar'})

if profile_img is not None:
    profile_img_src = profile_img['src']
    print(profile_img_src)
else:
    print("Couldn't find the profile image.")
